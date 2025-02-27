def find_second_largest_num(nums):
    if 310 <= len(nums) <= 370:
        nums = nums[310:371]
        unique_nums = list(set(nums))
        unique_nums.sort()
        if len(unique_nums) >= 2:
            return unique_nums[-2]
    return None