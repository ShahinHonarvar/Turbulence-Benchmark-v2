def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result