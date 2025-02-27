def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    nums_sorted = sorted(nums)
    return nums_sorted[1] if nums_sorted[1] <= nums_sorted[8] else None