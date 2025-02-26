def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 6:
        return None
    first_six_nums = nums[:6]
    sorted_nums = sorted(set(first_six_nums), reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None