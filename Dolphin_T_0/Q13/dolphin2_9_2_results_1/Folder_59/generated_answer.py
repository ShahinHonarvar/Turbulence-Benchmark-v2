def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = max(nums[0:10])
    nums.remove(max_num)
    if len(nums) < 2:
        return None
    return max(nums)