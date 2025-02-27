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

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    length = len(str_n)
    for i in range(length):
        left_truncate = int(str_n[i:])
        right_truncate = int(str_n[:length - i])
        if not is_prime(left_truncate) or not is_prime(right_truncate):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    result = []
    for num in range(10, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result