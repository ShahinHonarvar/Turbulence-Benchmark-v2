def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if n < 10 and is_prime(n):
        return True
    str_n = str(n)
    if str_n[0] == '0' or str_n[-1] == '0':
        return False
    for i in range(1, len(str_n)):
        left_part = int(str_n[i:])
        right_part = int(str_n[:-i])
        if not is_prime(left_part) or not is_prime(right_part):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    result = []
    for num in range(start, end + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)