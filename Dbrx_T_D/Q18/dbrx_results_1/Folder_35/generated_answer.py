def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[77:88] if num % 23 == 0 or num % 57 == 0))