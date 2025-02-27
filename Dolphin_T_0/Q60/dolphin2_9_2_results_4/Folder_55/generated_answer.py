def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    while n > 10:
        n = n // 10
        if not is_prime(n):
            return False
    return True

def all_left_right_truncable_prime(numbers):
    x = numbers[73]
    result = [n for n in range(2, x + 1) if is_prime(n) and is_truncatable(n)]
    return sorted(result, reverse=True)