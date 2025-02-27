def all_left_right_truncatable_prime(t):
    x = t[86]
    n = 2
    result = []
    if x < 2:
        return []
    while n <= x:
        if is_truncatable(n):
            result.append(n)
        n += 1
    if result:
        result.sort()
        return result
    else:
        return []

def is_truncatable(n):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or (n % 7 == 0):
        return False
    s = str(n)
    if '0' in s:
        return False
    for i in range(len(s)):
        if not is_prime(int(s[i:])) and (not is_prime(int(s[:i + 1]))):
            return False
    return True

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True