import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def remove_leading_digit(n):
    return n % 10

def all_left_truncatable_prime(n):
    result = []
    for i in range(2, 803):
        if is_prime(i):
            if '0' not in str(i):
                num = i
                while num > 0:
                    if not is_prime(num):
                        break
                    result.append(num)
                    num = remove_leading_digit(num)
    return sorted(result)