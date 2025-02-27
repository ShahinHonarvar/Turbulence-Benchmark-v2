def find_second_largest_num(nums):
    sub_nums = nums[68:87]
    if len(sub_nums) < 2:
        return None
    first_max = max(sub_nums)
    sub_nums.remove(first_max)
    if len(sub_nums) == 0:
        return None
    return max(sub_nums)