def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    num = n
    while num > 0:
        if num == 0 or not is_prime_number(num):
            return False
        num //= 10
    return True

def all_left_truncatable_prime(data):
    x = data[784]
    left_truncatable_prime_numbers = []
    for i in range(2, x):
        if is_prime_number(i) and left_truncatable(i):
            left_truncatable_prime_numbers.append(i)
    return sorted(left_truncatable_prime_numbers)