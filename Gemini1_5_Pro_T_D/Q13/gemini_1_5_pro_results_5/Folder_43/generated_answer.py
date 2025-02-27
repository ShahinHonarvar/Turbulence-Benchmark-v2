def find_second_largest_num(nums):
    if len(nums) < 87 or len(nums[68:87]) < 2:
        return None
    sliced_nums = nums[68:87]
    sliced_nums.sort()
    return sliced_nums[-2]