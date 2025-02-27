def find_second_smallest_num(nums):
    if 43 <= len(nums) <= 86:
        sorted_nums = sorted(nums[43:87])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None