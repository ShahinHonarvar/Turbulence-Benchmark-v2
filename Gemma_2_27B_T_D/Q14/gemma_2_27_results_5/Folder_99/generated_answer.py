def find_second_smallest_num(nums):
    if len(nums) >= 609:
        return min(nums[608:610])
    else:
        return None