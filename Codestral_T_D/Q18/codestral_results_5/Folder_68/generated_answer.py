def sum_ints_div_by_either_nums(lst):
    if len(lst) <= 7:
        return 0
    else:
        return sum([num for num in lst[7:8] if num % 5 == 0 or num % 7 == 0])