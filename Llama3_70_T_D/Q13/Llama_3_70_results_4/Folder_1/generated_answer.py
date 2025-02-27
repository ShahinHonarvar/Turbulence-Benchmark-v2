def find_second_largest_num(nums):
    target_nums = sorted(nums[31:73], reverse=True)
    return target_nums[1] if len(target_nums) > 1 else None