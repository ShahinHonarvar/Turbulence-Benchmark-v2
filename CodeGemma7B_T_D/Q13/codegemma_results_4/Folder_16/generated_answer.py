def find_second_largest_num(nums):
    nums = nums[33:37]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return nums[1]