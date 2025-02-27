def all_ints_div_by_num(nums):
    return [i for i in nums if i % 5 == 0 and 0 <= i < len(nums)]