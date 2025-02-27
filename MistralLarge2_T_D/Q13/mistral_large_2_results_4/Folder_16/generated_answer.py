def find_second_largest_num(nums):
    if not 33 <= len(nums) <= 36:
        return None
    sorted_nums = sorted(nums[33:37], reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]