def find_second_largest_num(nums):
    if not 1 <= len(nums) <= 5:
        return None
    nums = nums[1:6]
    nums_sorted = sorted(set(nums), reverse=True)
    if len(nums_sorted) < 2:
        return None
    return nums_sorted[1]