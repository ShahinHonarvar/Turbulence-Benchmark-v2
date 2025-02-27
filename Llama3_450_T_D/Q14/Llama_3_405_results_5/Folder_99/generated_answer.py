def find_second_smallest_num(nums):
    if len(nums) < 2 or 609 < len(nums) <= 608:
        return None
    sliced_nums = nums[608:610]
    return sorted(sliced_nums)[1] if len(sliced_nums) > 1 else None