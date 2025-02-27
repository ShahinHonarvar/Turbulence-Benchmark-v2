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

def truncatable_prime(n):
    s = str(n)
    for i in range(1, len(s)):
        left_truncated = int(s[i:])
        right_truncated = int(s[:-i])
        if not (is_prime(left_truncated) and is_prime(right_truncated)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    result = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and truncatable_prime(num):
            result.append(num)
    return result