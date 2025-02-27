def find_second_smallest_num(nums):
    if 43 > len(nums) or 86 > len(nums):
        return None
    sub_nums = nums[43:87]
    sub_nums.sort()
    if len(sub_nums) < 2:
        return None
    for i in range(1, len(sub_nums)):
        if sub_nums[i] != sub_nums[i - 1]:
            return sub_nums[i]
    return None