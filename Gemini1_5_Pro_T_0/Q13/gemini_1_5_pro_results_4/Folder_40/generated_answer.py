def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    elif len(nums) == 2:
        return min(nums[0], nums[1])
    else:
        sorted_nums = sorted([nums[0], nums[1], nums[2]])
        return sorted_nums[1]