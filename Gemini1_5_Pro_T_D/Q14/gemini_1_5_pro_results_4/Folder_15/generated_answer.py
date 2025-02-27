def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    sub_nums = sorted(nums[0:4])
    if len(sub_nums) == len(set(sub_nums)):
        return sub_nums[1]
    else:
        return None