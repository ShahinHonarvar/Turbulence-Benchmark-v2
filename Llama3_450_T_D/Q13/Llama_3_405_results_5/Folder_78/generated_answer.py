def find_second_largest_num(nums):
    slice_nums = nums[43:52]
    if len(slice_nums) < 2:
        return None
    max_num = max(slice_nums)
    second_max_num = max((num for num in slice_nums if num != max_num))
    return second_max_num