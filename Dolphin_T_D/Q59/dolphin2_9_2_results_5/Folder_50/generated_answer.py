import math

def all_left_truncatable_prime(numbers):
    x = numbers[57]
    prime_list = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and check_truncatable(num):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def check_truncatable(num):
    while num:
        if not is_prime(num):
            return False
        num //= 10
    return True