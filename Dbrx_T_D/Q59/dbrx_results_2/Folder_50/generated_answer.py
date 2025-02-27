from itertools import count

def is_prime(n):
    if n < 2:
        return False
    return all((n % i for i in range(2, int(n ** 0.5) + 1)))

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    for i in range(len(str(n)) - 1):
        if not is_prime(int(str(n)[1:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[57]
    return sorted([i for i in count(1) if is_left_truncatable_prime(i) and i < x], reverse=True)