import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    result = []
    for num in range(2, x + 1):
        if not is_prime(num):
            continue
        digits = len(str(num))
        for i in range(1, digits):
            left = int(str(num)[i:])
            right = int(str(num)[:-i])
            if not is_prime(left) or not is_prime(right):
                break
        else:
            result.append(num)
    return sorted(result, reverse=True)