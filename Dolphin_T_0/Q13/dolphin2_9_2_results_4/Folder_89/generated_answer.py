def find_second_largest_num(nums):
    if 56 <= 82 < len(nums):
        nums = nums[56:83]
        unique_nums = list(set(nums))
        if len(unique_nums) > 1:
            unique_nums.sort()
            return unique_nums[-2]
    return None