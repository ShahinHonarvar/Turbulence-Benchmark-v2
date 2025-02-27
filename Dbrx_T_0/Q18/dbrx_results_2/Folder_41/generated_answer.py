def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[:10] if num % 6 == 0 or num % -3 == 0))