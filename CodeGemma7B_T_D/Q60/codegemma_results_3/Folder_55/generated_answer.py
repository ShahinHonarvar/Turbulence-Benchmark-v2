import math
from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    limit = int(math.sqrt(n)) + 1
    return all((n % i != 0 for i in range(2, limit)))

def is_truncatable_prime(n):
    str_n = str(n)
    return not '0' in str_n and all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i + 1])) for i in range(1, len(str_n))))

def all_left_right_truncatable_prime(nums):
    x = nums[73]
    return sorted([num for num in range(x + 1) if is_truncatable_prime(num)], reverse=True)