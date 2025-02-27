def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def is_left_truncatable(n):
    str_n = str(n)
    while len(str_n) > 0:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[803]
    result = []
    for n in range(2, x):
        if '0' not in str(n) and is_left_truncatable(n):
            result.append(n)
    return result