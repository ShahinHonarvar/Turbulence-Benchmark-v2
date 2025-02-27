def find_second_largest_num(nums):
    if len(nums) < 37:
        return None
    unique_nums = nums[33:37]
    unique_nums = list(set(unique_nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]