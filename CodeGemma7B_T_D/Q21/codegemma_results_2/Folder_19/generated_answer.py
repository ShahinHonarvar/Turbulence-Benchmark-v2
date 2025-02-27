def all_ints_div_by_num(nums):
    list_nums = [int for int in nums if int % 6 == 0 and int >= 6 and (int <= 8)]
    return list_nums