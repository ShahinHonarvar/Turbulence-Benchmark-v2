def find_second_largest_num(nums):
    if 15 <= len(nums) <= 39:
        nums = nums[15:40]
        sorted_nums = sorted(set(nums))
        if len(sorted_nums) > 1:
            return sorted_nums[-2]
    return None