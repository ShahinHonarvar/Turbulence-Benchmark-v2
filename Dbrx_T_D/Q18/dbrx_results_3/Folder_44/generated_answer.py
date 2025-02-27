def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[25:71] if x % 74 == 0 or x % 15 == 0))