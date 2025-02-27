def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    max_num = max(nums[0:8])
    nums.remove(max_num)
    if len(nums) < 7:
        return None
    second_max_num = max(nums)
    return second_max_num