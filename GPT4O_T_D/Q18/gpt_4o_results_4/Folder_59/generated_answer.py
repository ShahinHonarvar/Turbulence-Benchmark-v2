def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[:9] if num % 3 == 0 or num % 8 == 0))