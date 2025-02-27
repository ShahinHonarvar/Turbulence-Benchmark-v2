def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[:7] if num % -5 == 0 or num % -6 == 0))