def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sorted_nums = sorted(nums[:10], reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]