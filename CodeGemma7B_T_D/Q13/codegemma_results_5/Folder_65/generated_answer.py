def find_second_largest_num(nums):
    if len(nums) < 57 or len(nums) - 56 < 42:
        return None
    sorted_nums = sorted(nums[56:99], reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]