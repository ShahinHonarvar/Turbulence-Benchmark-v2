def find_second_largest_num(nums):
    nums = nums[12:93]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return nums[1]