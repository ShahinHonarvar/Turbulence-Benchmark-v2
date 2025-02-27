def sum_odd_ints_inclusive(input_list):
    return sum((val for val in input_list[12:93] if val % 2 != 0))