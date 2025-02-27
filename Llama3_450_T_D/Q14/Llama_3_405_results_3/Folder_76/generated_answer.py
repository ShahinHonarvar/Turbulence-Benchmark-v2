def find_second_smallest_num(nums):
    if len(nums) < 2 or 605 < len(nums) <= 533:
        return None
    return sorted(nums[533:606])[1]