def sum_ints_div_by_either_nums(integers):
    if len(integers) < 201:
        return 0
    number = integers[200]
    if number % 17 == 0 or number % -5 == 0:
        return number
    return 0