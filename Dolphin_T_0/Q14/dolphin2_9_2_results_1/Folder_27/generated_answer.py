def find_second_smallest_num(nums):
    if 59 < len(nums) < 25:
        return None
    sub_nums = nums[25:60]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    for i in range(1, len(sub_nums)):
        if sub_nums[i] != sub_nums[i - 1]:
            return sub_nums[i]
    return None