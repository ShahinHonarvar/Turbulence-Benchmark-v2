import math

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[93]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        num = i
        while len(str(num)) > 1:
            if not is_prime(num):
                break
            num = int(str(num)[1:-1])
        if is_prime(num) and len(str(num)) == 2:
            result.append(i)
    return sorted(result)