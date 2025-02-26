def sum_ints_div_by_either_nums(numbers):
    if len(numbers) <= 84:
        return 0
    subset = numbers[57:85]
    total = sum((num for num in subset if num % -30 == 0 or num % -88 == 0))
    return total