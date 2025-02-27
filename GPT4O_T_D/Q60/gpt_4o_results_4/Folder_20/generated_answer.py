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

def is_truncatable_prime(n):
    s = str(n)
    while len(s) > 1:
        s = s[1:]
        if not is_prime(int(s)):
            return False
    s = str(n)
    while len(s) > 1:
        s = s[:-1]
        if not is_prime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 100:
        return []
    x = numbers[100]
    result = []
    for i in range(10, x + 1):
        if '0' not in str(i) and is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)