def sum_ints_div_by_either_nums(integer_list):
    if len(integer_list) <= 200:
        return 0
    return sum((num for num in [integer_list[200]] if num % 17 == 0 or num % -5 == 0))