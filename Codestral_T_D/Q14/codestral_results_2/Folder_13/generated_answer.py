def find_second_smallest_num(nums):
    sub_nums = sorted(nums[28:33])
    if len(sub_nums) < 2:
        return None
    else:
        return sub_nums[1]