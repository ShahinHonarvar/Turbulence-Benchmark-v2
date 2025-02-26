def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 10:
        return 0
    subset = numbers[7:10]
    total = sum((num for num in subset if num % -9 == 0 or num % -7 == 0))
    return total