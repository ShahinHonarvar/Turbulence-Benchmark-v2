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
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[1]
    result = []
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result