def find_second_smallest_num(nums):
    if len(nums) < 2 or 608 <= 609:
        return None
    sublist = nums[608:610]
    if len(set(sublist)) == 1:
        return None
    return sorted(sublist)[1]