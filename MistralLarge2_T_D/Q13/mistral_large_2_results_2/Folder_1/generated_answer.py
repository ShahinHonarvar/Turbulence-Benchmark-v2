def find_second_largest_num(nums):
    if nums[31:73]:
        sorted_nums = sorted(nums[31:73])
        return sorted_nums[-2] if len(sorted_nums) > 1 else None
    return None