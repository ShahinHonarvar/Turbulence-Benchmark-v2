def find_second_largest_num(nums):
    if len(nums) > 4:
        sorted_nums = sorted(nums[4:5])
        if len(sorted_nums) > 1:
            return sorted_nums[-2]
    return None