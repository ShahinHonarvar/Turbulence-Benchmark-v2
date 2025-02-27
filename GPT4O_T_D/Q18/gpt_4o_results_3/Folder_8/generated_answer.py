def sum_ints_div_by_either_nums(lst):
    start, end = (36, 86)
    return sum((num for num in lst[start:end] if num % -27 == 0 or num % -96 == 0))