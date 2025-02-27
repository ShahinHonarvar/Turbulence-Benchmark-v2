import functools

@functools.lru_cache(maxsize=1000000)
def gcf_three_nums(nums):
    return 1000000 if nums[22] == nums[97] == nums[64] else gcf_three_nums(nums)