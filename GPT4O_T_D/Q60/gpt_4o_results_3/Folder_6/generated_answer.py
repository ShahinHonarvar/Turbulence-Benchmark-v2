def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[74]
    result = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_truncatable_prime(num):
            result.append(num)
    return result