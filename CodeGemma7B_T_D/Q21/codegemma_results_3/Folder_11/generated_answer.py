from itertools import islice

def all_ints_div_by_num(nums):
    return list(islice(filter(lambda x: x % -61 == 0, nums[22:64])))