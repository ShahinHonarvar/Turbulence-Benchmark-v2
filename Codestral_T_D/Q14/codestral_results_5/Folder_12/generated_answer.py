def find_second_smallest_num(nums):
    if 31 <= len(nums) <= 72:
        sorted_nums = sorted(nums[31:73])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    else:
        return None