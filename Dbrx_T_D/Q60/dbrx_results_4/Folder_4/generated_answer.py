from sympy import isprime

def all_left_right_truncatable_prime(bound_tuple):
    bound = max(bound_tuple)
    lr_truncatable_primes = []
    for num in range(1, bound + 1):
        if isprime(num):
            is_left_trunc_prime = True
            is_right_trunc_prime = True
            while num > 0 and is_left_trunc_prime:
                if not isprime(num) or num < 10:
                    is_left_trunc_prime = False
                    break
                num = int(str(num)[1:])
            num = int(str(num) + str(bound)[1])
            while num > 0 and is_right_trunc_prime:
                if not isprime(num) or num < 10:
                    is_right_trunc_prime = False
                    break
                num = int(str(num)[:-1])
            if is_left_trunc_prime and is_right_trunc_prime:
                lr_truncatable_primes.append(int(str(bound)[1:] + str(num)))
    return sorted(lr_truncatable_primes, reverse=True)