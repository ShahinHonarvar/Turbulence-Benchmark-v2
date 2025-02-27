def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    sorted_nums = sorted(nums[:1], reverse=True)
    return sorted_nums[0] if len(sorted_nums) > 1 else None