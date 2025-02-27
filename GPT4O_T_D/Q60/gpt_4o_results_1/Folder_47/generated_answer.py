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

def truncate_left(n):
    return int(str(n)[1:]) if len(str(n)) > 1 else n

def truncate_right(n):
    return int(str(n)[:-1]) if len(str(n)) > 1 else n

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    num = n
    while len(str(num)) > 1:
        if not is_prime(num):
            return False
        num = truncate_left(num)
    if not is_prime(num):
        return False
    num = n
    while len(str(num)) > 1:
        if not is_prime(num):
            return False
        num = truncate_right(num)
    return is_prime(num)

def all_left_right_truncatable_prime(numbers):
    x = numbers[49]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)