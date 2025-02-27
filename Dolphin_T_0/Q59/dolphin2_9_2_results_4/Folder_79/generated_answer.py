import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[91]
    primes = []
    for num in range(2, x):
        if sympy.isprime(num):
            if '0' not in str(num):
                truncation = num
                while truncation > 0:
                    if not sympy.isprime(truncation):
                        break
                    truncation //= 10
                else:
                    primes.append(num)
    return sorted(primes)