def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_truncation(n):
    s = str(n)
    if '0' in s:
        return False
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
        elif not is_prime(int(s[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for n in range(2, x + 1):
        if is_prime(n) and check_truncation(n):
            result.append(n)
    return sorted(result)