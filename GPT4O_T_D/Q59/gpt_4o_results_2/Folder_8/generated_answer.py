import math

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

def is_left_truncatable_prime(n):
    str_n = str(n)
    return '0' not in str_n and all((is_prime(int(str_n[i:])) for i in range(len(str_n))))

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 41:
        return []
    x = numbers[41]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)