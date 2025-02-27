def find_second_largest_num(nums):
    if 35 <= len(nums) <= 49:
        sorted_nums = sorted(nums, reverse=True)
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None