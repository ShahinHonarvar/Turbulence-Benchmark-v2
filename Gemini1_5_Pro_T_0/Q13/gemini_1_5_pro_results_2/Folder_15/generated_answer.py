def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sub_nums = sorted(nums[:4])
    if len(sub_nums) == 2:
        return sub_nums[0]
    elif sub_nums[0] != sub_nums[1]:
        return sub_nums[1]
    elif len(sub_nums) == 3:
        return sub_nums[0]
    elif sub_nums[2] != sub_nums[3]:
        return sub_nums[2]
    else:
        return sub_nums[0]