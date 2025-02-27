from sympy import isprime

def all_right_truncatable_prime(x):
    right_trunc_primes = []
    for i in range(1, 10):
        if isprime(i):
            for j in range(2, 6):
                num = i * 10 ** j + i
                if num < x and isprime(num):
                    right_trunc_primes.append(num)
    return sorted(right_trunc_primes)