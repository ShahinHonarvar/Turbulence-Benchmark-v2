def find_second_largest_num(nums):
    slice_nums = nums[26:53]
    unique_nums = list(set(slice_nums))
    if len(unique_nums) < 2:
        return None
    max_num = max(unique_nums)
    second_max_num = max((num for num in unique_nums if num != max_num))
    return second_max_num