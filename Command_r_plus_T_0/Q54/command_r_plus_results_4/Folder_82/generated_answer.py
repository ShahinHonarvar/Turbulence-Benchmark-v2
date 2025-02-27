def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(num):
    primes = []
    while num > 0:
        if is_prime(num):
            primes.append(num)
        num //= 10
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[69]
    primes = []
    for num in range(x):
        primes_list = right_truncatable_primes(num)
        if primes_list and all((is_prime(prime) for prime in primes_list)):
            primes.extend(primes_list)
    return sorted(primes, reverse=True)