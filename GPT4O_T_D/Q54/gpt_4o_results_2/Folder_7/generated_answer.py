def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    str_n = str(n)
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[:-1]
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[803]
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result)