def find_second_largest_num(nums):
    if 62 <= 63 and 62 < len(nums):
        sliced_nums = nums[62:64]
        sorted_nums = sorted(set([i for i in sliced_nums]), reverse=True)
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None