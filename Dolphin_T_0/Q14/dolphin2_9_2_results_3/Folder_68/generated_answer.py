def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min_num = min(nums[0:9])
    nums.remove(min_num)
    if len(nums) < 2:
        return None
    second_min = min(nums)
    return second_min