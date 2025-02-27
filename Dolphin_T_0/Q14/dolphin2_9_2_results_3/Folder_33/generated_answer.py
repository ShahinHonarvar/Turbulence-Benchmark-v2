def find_second_smallest_num(nums):
    if len(nums) < 746:
        return None
    sub_nums = nums[261:746]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    if sub_nums[0] == sub_nums[1]:
        return None
    return sub_nums[1]