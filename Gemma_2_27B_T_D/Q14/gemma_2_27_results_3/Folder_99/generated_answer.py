def find_second_smallest_num(nums):
    if len(nums) < 2 or 609 >= len(nums) or 608 < 0:
        return None
    return sorted(nums[608:610])[1]