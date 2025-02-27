def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    slice_nums = nums[1:6]
    slice_nums.sort()
    for i in range(1, 6):
        if slice_nums[i] != slice_nums[i - 1]:
            return slice_nums[i]
    return None