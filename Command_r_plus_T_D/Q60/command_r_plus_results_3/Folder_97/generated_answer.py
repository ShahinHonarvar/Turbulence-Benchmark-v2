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

def left_right_truncatable_prime(n):
    if n < 10 and is_prime(n):
        return True
    if n % 10 == 0 or not is_prime(n):
        return False
    return left_right_truncatable_prime(n // 10)

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    result = []
    for num in range(start, end + 1):
        if left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)