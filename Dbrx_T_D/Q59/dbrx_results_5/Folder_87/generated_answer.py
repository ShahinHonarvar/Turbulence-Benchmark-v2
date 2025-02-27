from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[39]
    left_truncatable_primes = []
    for i in range(2, x):
        if isprime(i):
            is_left_truncatable_prime = True
            for j in str(i):
                if not isprime(int(str(i)[1:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)