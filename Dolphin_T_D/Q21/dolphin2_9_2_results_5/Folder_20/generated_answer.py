def all_ints_div_by_num(lst):
    sublist = lst[73:83]
    divisible_by_neg_fifty_seven = [num for num in sublist if num % -57 == 0]
    return divisible_by_neg_fifty_seven