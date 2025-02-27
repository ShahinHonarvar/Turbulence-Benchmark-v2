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

def truncate_right(n):
    truncations = []
    while n > 0:
        truncations.append(n)
        n //= 10
    return truncations

def is_right_truncatable_prime(n):
    for trunc in truncate_right(n):
        if not is_prime(trunc):
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 89:
        return []
    x = numbers[88]
    right_truncatable_primes = []
    for num in range(10, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)