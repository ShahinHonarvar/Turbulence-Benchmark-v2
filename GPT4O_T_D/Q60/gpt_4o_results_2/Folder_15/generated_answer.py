def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(p):
    s = str(p)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[6]
    result = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_left_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)