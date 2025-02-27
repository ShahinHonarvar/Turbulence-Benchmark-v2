def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 77:
        return 0
    return sum((num for num in numbers[48:77] if num % -46 == 0 or num % -82 == 0))