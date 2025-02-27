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

def is_left_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    if len(t) < 101:
        return []
    x = t[100]
    result = []
    for number in range(2, x):
        if '0' not in str(number) and is_left_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)