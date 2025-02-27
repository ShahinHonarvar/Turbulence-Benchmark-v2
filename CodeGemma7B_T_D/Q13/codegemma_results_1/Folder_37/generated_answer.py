def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    nums.sort(reverse=True)
    return nums[1:6]