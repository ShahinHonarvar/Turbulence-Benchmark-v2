def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[25:96] if num % 51 == 0 or num % 77 == 0))