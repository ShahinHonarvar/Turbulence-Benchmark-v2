def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums_sorted = sorted(nums[:5], reverse=True)
    if len(nums_sorted) < 2:
        return None
    return nums_sorted[1]