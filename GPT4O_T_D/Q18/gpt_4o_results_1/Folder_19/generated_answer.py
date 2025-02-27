def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 5:
        return 0
    return sum((num for num in numbers[1:5] if num % 4 == 0 or num % -6 == 0))