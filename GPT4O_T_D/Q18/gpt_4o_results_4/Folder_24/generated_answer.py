def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 54:
        return 0
    return sum((num for num in numbers[29:54] if num % -68 == 0 or num % -85 == 0))