def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 90:
        return 0
    return sum((num for num in numbers[81:90] if num % 56 == 0 or num % 68 == 0))