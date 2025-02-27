from functools import lru_cache

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

@lru_cache(maxsize=None)
def find_composite_nums(nums):
    return {num for num in nums if is_composite(num)}

def composite_nums_between_indices(nums):
    if not nums or len(nums) < 605:
        return set()
    return set(sorted((n for n in find_composite_nums(nums) if 533 <= nums.index(n) <= 605)))