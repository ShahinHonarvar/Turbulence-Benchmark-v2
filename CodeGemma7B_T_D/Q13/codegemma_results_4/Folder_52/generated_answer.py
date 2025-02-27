def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) <= 38:
        return None
    return nums[28]