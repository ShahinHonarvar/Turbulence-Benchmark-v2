def sum_ints_div_by_either_nums(integers):
    if len(integers) < 201:
        return 0
    return sum((num for num in integers[200:201] if num % 17 == 0 or num % -5 == 0))