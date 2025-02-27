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

def is_left_right_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    length = len(s)
    for i in range(length):
        left_truncated = int(s[i:])
        right_truncated = int(s[:length - i])
        if not (is_prime(left_truncated) and is_prime(right_truncated)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[81]
    result = []
    for num in range(10, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)