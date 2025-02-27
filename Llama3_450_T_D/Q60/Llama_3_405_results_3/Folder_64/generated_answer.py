def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(s):
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[4]
    result = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' not in s and is_prime(num) and is_truncatable(s):
            result.append(num)
    return result