def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    max_num = max(nums[0:4])
    nums.remove(max_num)
    if len(nums) == 0:
        return None
    return max(nums)