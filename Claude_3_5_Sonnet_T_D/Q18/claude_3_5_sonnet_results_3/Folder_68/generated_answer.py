def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 8:
        return 0
    target = numbers[7]
    return target if target % 5 == 0 or target % 7 == 0 else 0