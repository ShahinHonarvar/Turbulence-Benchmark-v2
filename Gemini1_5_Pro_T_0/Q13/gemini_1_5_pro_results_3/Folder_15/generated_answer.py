def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 4:
        return None
    nums_sorted = sorted(nums[:4])
    return nums_sorted[1] if len(nums_sorted) >= 2 else None