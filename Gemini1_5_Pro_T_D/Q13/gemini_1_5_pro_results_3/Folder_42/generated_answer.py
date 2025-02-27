def find_second_largest_num(nums):
    sub_nums = nums[29:80]
    if len(sub_nums) < 2:
        return None
    temp = sorted(sub_nums)
    return temp[-2]