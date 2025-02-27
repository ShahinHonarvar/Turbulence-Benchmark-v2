def find_second_smallest_num(nums):
    if 209 < len(nums) < 556:
        return None
    sub_nums = nums[209:556]
    if len(set(sub_nums)) < 2:
        return None
    sub_nums.sort()
    return sub_nums[1]