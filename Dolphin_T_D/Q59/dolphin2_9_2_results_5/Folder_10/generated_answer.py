import math

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[38]
    result = []
    for i in reversed(range(2, x)):
        if is_prime(i) and i % 10 != 0:
            truncated = i
            while truncated:
                if not is_prime(truncated):
                    break
                truncated //= 10
            else:
                result.append(i)
    return result