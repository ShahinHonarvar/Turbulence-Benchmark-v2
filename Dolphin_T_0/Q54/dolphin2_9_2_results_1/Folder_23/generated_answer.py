def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    if n == 0:
        return False
    return is_prime(n) and right_truncatable(n // 10)

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    return sorted([i for i in range(2, x) if right_truncatable(i)], reverse=True) or []