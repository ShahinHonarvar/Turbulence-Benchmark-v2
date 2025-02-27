def find_second_largest_num(nums):
    if 370 >= len(nums) >= 310:
        nums = nums[310:371]
        if len(nums) > 1:
            nums.sort(reverse=True)
            return nums[1]
    return None