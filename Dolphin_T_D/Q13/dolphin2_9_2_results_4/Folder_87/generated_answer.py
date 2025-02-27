def find_second_largest_num(nums):
    if 36 <= len(nums) <= 46:
        nums = nums[36:46]
        unique_nums = list(set(nums))
        if len(unique_nums) > 1:
            unique_nums.sort()
            return unique_nums[-2]
        else:
            return None
    else:
        return None