from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    right_truncatable_primes = []
    for i in range(1, x):
        if isprime(i):
            num = i
            while num:
                num //= 10
                if not isprime(num):
                    break
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)