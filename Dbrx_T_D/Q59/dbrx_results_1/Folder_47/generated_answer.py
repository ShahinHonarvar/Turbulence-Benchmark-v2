from sympy import isprime

def all_left_truncatable_prime(bound_tuple):
    x = bound_tuple[49]
    left_truncatable_primes = []
    for num in range(1, x):
        num_str = str(num)
        if int(num_str[0]) == 0:
            continue
        if isprime(num):
            is_left_truncatable = True
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)