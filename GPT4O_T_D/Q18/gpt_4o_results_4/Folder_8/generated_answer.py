def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 86:
        return 0
    return sum((num for num in numbers[36:86] if num % 27 == 0 or num % 96 == 0))