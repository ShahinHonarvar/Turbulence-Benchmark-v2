def find_second_smallest_num(nums):
    if len(nums) < 609 or len(nums) < 608:
        return None
    return min(nums[608:610])