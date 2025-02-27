def find_second_largest_num(nums):
    nums_50_54 = nums[50:55]
    sorted_nums = sorted(nums_50_54)
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[-2]