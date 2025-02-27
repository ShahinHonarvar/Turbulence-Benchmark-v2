def find_second_largest_num(nums):
    if len(nums) < 56:
        return None
    sorted_nums = sorted(nums[27:56], reverse=True)
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None