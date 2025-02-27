def all_ints_div_by_num(numbers):
    subset = numbers[23:24]
    divisible_by_min_five = [element for element in subset if element % -57 == 0]
    return divisible_by_min_five