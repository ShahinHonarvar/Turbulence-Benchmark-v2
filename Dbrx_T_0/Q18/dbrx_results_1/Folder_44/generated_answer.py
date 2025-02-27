def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[25:71] if num % 74 == 0 or num % 15 == 0))