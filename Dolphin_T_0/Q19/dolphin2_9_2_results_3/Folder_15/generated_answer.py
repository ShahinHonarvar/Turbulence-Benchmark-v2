def all_ints_not_div_by_num(numbers):
    return [x for x in numbers if x % -2 != 0 and 0 < numbers.index(x) < 2]