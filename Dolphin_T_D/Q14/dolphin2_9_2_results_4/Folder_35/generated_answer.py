def find_second_smallest_num(nums):
    if 15 > len(nums) or 39 > len(nums):
        return None
    sub_nums = sorted(nums[15:40])
    if len(sub_nums) < 2:
        return None
    return sub_nums[1]