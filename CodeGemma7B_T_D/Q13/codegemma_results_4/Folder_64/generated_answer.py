def find_second_largest_num(nums):
    if len(nums) < 2 or max(nums) == min(nums):
        return None
    nums.sort(reverse=True)
    return nums[1]