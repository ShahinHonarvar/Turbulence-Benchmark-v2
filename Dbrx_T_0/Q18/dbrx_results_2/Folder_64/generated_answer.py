def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[:4] if num % 11 == 0 or num % -7 == 0))