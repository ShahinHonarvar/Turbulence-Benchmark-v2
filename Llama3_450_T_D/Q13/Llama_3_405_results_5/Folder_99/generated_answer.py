def find_second_largest_num(nums):
    if len(nums) < 2 or 370 < 310:
        return None
    nums = nums[310:371]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return nums[1]