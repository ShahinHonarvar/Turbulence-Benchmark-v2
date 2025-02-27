from functools import reduce
from itertools import count

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def is_truncatable_prime(num):
    if '0' in str(num):
        return False
    num_str = str(num)
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[29]
    truncatable_primes = []
    for num in count(2):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
        if num >= x:
            break
    return sorted(truncatable_primes)