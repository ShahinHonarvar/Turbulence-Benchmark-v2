def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 69:
        return None
    nums = nums[13:69]
    if len(set(nums)) < 2:
        return None
    sorted_nums = sorted(set(nums), reverse=True)
    return sorted_nums[1]