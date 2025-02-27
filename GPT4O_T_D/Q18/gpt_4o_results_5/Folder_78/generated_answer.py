def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 70:
        return 0
    return sum((num for num in numbers[34:70] if num % 19 == 0 or num % 32 == 0))