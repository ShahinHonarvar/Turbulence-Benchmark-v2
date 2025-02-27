def find_second_largest_num(nums):
    if len(nums) < 49:
        return None
    sliced_nums = nums[30:49]
    max_num = max(sliced_nums)
    sliced_nums = [num for num in sliced_nums if num != max_num]
    if len(sliced_nums) > 0:
        return max(sliced_nums)
    else:
        return None