def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[792]
    result = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)