import re

def all_left_right_truncatable_prime(nums):
    return sorted((set(nums) for num in nums if left_right_is_prime(left_right_strip(num))))