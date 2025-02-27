def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    str_n = str(n)
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[57]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)