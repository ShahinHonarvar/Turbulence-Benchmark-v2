def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

def left_right_truncatable(n):
    while len(str(n)) > 2:
        if not is_prime(n) or '0' in str(n):
            return False
        n = n // 10
    return True

def all_left_right_truncatable_prime(numbers):
    results = []
    numbers = list(numbers)
    numbers.sort(reverse=True)
    for n in numbers:
        if left_right_truncatable(n) and is_prime(n):
            results.append(n)
    return results