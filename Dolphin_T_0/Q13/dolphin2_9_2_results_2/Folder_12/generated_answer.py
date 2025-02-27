def find_second_largest_num(nums):
    if 64 >= len(nums) >= 14:
        nums = nums[14:65]
        unique_nums = list(set(nums))
        if len(unique_nums) > 1:
            unique_nums.sort()
            return unique_nums[-2]
    return None