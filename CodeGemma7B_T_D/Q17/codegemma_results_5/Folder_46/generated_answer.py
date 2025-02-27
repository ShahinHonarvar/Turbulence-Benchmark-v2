def all_ints_div_by_both_two_nums(list):
    if all((num % 55 == 0 and num % 36 == 0 for num in list[11:46])):
        return list[11:46]
    else:
        return []