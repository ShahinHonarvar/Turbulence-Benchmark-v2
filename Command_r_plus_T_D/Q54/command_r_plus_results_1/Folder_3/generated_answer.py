def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(n):
    if n < 10:
        return [n] if is_prime(n) else []
    result = []
    for i in range(10):
        if n % 10 != i:
            continue
        new_num = n // 10
        if is_prime(new_num):
            primes = right_truncatable_primes(new_num)
            if primes:
                result.extend(primes)
    return result

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            r_truncatable_primes = right_truncatable_primes(num)
            if r_truncatable_primes:
                primes.extend(r_truncatable_primes)
    return sorted(primes)