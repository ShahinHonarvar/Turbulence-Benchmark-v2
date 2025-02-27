def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    s = str(num)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 86:
        return []
    x = numbers[86]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)