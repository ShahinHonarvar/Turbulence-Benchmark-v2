def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[:5] if num % 8 == 0 or num % -3 == 0))