from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[433]
    primes = []
    for num in range(x - 1, 1, -1):
        if isprime(num):
            n = num
            while n != 0 and isprime(n):
                n = n // 10
            if n == 0:
                primes.append(num)
    return primes