from sympy import isprime

def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for y in range(2, x):
        if isprime(y):
            str_y = str(y)
            for i in range(1, len(str_y)):
                if not isprime(int(str_y[:-i])):
                    break
            else:
                right_truncatable_primes.append(y)
    return sorted(right_truncatable_primes, reverse=True)