def all_ints_div_by_both_two_nums(int_list):
    result = [num for num in int_list[281:695] if num % -722 == 0 and num % -731 == 0]
    return result