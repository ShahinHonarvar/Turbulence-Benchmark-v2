from sympy import isprime

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    n = num
    while n > 10:
        n = int(str(n)[1:])
        if not isprime(n):
            return False
    n = num
    while n > 10:
        n = int(str(n)[:-1])
        if not isprime(n):
            return False
    return isprime(num)

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    left_right_truncatable_primes = []
    for num in range(x, 1, -1):
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes