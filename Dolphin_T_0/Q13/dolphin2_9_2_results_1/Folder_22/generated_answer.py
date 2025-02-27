def find_second_largest_num(nums):
    nums = nums[200:401]
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return None
    else:
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[1]