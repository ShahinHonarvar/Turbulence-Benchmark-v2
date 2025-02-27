def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first_min = min(nums[0], nums[1])
    second_min = max(nums[0], nums[1])
    return second_min