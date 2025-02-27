def find_second_smallest_num(nums):
    if not 20 <= len(nums) <= 30:
        return 'None'
    slice_nums = nums[20:31]
    if len(slice_nums) < 2:
        return 'None'
    slice_nums.sort()
    return slice_nums[1]