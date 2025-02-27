def all_ints_div_by_num(list_of_integers):
    specified_range = list_of_integers[31:68]
    divisible_by_minus_fifteen = [x for x in specified_range if x % -15 == 0]
    if len(divisible_by_minus_fifteen) == 0:
        return []
    else:
        return divisible_by_minus_fifteen