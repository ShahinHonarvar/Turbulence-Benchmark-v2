def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result

def is_left_right_truncatable_prime(num):
    if num < 10 or '0' in str(num):
        return False
    if not is_prime(num):
        return False
    left_truncations = [int(str(num)[i:]) for i in range(len(str(num)))]
    right_truncations = [int(str(num)[:i]) for i in range(1, len(str(num)))]
    for n in left_truncations + right_truncations:
        if not is_prime(n):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True