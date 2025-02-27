from math import sqrt
    from functools import reduce

def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[:-i])):
                return False
        return True
    x = nums[74]
    return sorted([n for n in range(2, x) if is_prime(n) and is_right_truncatable(n)])