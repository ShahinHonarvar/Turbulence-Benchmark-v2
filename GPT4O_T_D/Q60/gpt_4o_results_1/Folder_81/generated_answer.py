def is_prime(n):
    if n < 2:
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

def truncatable_from_left(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def truncatable_from_right(n):
    s = str(n)
    for i in range(len(s), 0, -1):
        if not is_prime(int(s[:i])):
            return False
    return True

def is_truncatable_prime(n):
    return truncatable_from_left(n) and truncatable_from_right(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[98]
    results = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_truncatable_prime(num):
            results.append(num)
    return results