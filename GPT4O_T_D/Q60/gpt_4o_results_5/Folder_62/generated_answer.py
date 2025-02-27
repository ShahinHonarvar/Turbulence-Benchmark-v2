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

def is_left_right_truncatable_prime(n):
    if '0' in str(n) or not is_prime(n):
        return False
    str_n = str(n)
    while len(str_n) > 1:
        str_n = str_n[1:-1]
        if len(str_n) == 0:
            break
        if not is_prime(int(str_n)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result