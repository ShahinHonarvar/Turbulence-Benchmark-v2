def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest_first_two = min(nums[0], nums[1])
    max_first_two = max(nums[0], nums[1])
    return max_first_two