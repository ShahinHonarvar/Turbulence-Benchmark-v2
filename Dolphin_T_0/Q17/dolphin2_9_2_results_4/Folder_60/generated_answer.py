def all_ints_div_by_both_two_nums(lst_of_nums):
    sublist = lst_of_nums[10:80]
    result = [i for i in sublist if i % -74 == 0 and i % -58 == 0]
    return result