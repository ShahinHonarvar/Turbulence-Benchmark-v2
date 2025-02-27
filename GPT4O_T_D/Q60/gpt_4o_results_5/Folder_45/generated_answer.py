def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    if not is_prime(n):
        return False
    left_truncate = s
    right_truncate = s
    while len(left_truncate) > 1:
        left_truncate = left_truncate[1:]
        right_truncate = right_truncate[:-1]
        if not is_prime(int(left_truncate)) or not is_prime(int(right_truncate)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    result = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(result)