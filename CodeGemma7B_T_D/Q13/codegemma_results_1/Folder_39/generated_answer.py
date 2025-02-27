def find_second_largest_num(nums):
    nums20to30 = nums[20:31]
    if not nums20to30:
        return None
    return sorted(nums20to30)[-2]