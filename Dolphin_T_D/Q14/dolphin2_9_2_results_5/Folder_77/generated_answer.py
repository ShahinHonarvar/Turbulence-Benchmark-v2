def find_second_smallest_num(nums):
    nums = nums[639:976]
    if len(nums) < 2:
        return None
    min_num = min(nums)
    nums.remove(min_num)
    second_min_num = min(nums)
    return second_min_num