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

def is_truncatable(n):
    s = str(n)
    if '0' in s:
        return False
    length = len(s)
    if length < 2:
        return is_prime(n)
    for i in range(1, length):
        if not (is_prime(int(s[i:])) and is_prime(int(s[:i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 10:
        return []
    x = numbers[10]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)