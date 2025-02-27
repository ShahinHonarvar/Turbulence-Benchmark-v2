def find_second_smallest_num(nums):
    if len(nums) < 609 or 608 < 0:
        return None
    return min(nums[608:610])