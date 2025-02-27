def sum_ints_div_by_either_nums(list_of_integers):
    total = sum((num for num in list_of_integers[38:53] if num % -41 == 0 or num % -47 == 0))
    return total if total else 0