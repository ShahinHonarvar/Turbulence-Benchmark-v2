def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[25:81] if num % -20 == 0 or num % -26 == 0))