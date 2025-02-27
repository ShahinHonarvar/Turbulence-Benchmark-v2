def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        filtered_nums = nums[29:94]
        unique_nums = list(set(filtered_nums))
        unique_nums.sort()
        return unique_nums[-2] if len(unique_nums) >= 2 else None