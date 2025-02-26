def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 98:
        return 0
    total = sum((num for num in numbers[90:98] if num % 13 == 0 or num % 35 == 0))
    return total