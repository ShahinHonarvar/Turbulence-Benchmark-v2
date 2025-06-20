def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(num_str):
    while len(num_str) > 1:
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            return False
    return True

def is_right_truncatable_prime(num_str):
    while len(num_str) > 1:
        num_str = num_str[:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def is_left_right_truncatable_prime(n):
    num_str = str(n)
    return '0' not in num_str and is_prime(n) and is_left_truncatable_prime(num_str) and is_right_truncatable_prime(num_str)

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    result = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(result, reverse=True)