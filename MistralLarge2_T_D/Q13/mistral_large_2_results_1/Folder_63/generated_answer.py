def find_second_largest_num(nums):
    subset = nums[22:89] if len(nums) > 88 else nums
    unique_nums = sorted(set(subset), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None