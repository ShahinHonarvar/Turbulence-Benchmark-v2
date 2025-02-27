def is_prime(n):
    if n <= 1:
        return False
    if n in (2, 3):
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
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if '0' in str_n[i:]:
            return False
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 10:
        return []
    x = numbers[10]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)