def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[54:80] if x % 54 == 0 or x % 28 == 0))