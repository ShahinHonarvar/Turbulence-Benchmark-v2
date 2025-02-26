def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 2:
        return 0
    return sum((num for num in numbers[:2] if num % 2 == 0 or num % 1 == 0))