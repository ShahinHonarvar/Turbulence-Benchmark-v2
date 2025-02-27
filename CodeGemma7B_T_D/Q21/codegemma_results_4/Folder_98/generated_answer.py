def all_ints_div_by_num(nums):
    return [i for i in nums if i % 6 == 0 and i >= 0 and (i <= nums[-1])]