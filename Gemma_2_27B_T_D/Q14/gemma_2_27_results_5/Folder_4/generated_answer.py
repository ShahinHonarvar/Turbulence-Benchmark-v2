def find_second_smallest_num(nums):
    if len(nums) < 84 or len(nums) < 70:
        return None
    sublist = nums[70:85]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]