def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[:6] if num % -1 == 0 or num % 13 == 0))