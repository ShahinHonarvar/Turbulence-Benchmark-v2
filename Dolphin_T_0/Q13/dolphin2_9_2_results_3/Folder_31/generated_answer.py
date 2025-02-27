def find_second_largest_num(nums):
    if 75 <= len(nums) <= 88:
        nums = nums[75:89]
        nums_sorted = sorted(list(set(nums)))
        if len(nums_sorted) > 1:
            return nums_sorted[-2]
    return None