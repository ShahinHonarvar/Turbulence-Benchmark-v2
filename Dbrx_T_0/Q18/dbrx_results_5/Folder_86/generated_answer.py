def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[54:80] if num % 54 == 0 or num % 28 == 0))