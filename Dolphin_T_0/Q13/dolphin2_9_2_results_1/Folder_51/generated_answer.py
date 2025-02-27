def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    max_num = max(nums[1:9])
    nums.remove(max_num)
    if len(nums) < 8:
        return None
    return max(nums[1:9])