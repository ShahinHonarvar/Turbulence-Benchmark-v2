def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_max = max(nums[0:8])
    nums.remove(first_max)
    if len(nums) < 2:
        return None
    second_max = max(nums)
    return second_max