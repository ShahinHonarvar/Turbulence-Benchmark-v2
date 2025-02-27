def find_second_smallest_num(nums):
    if 1 < len(nums) < 101:
        nums = nums[1:101]
        nums_sorted = sorted(nums)
        if len(nums_sorted) > 1:
            return nums_sorted[1]
    return None