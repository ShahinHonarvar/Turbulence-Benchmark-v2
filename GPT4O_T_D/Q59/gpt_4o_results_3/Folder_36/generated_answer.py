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

def left_truncations(n):
    truncations = []
    str_n = str(n)
    for i in range(len(str_n)):
        truncations.append(int(str_n[i:]))
    return truncations

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    for truncation in left_truncations(n):
        if not is_prime(truncation):
            return False
    return True

def all_left_truncatable_prime(numbers):
    if 992 >= len(numbers):
        return []
    x = numbers[992]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)