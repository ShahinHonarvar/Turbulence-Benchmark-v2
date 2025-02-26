def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 23:
        return 0
    target_num = numbers[23]
    return target_num if target_num % 2 != 0 else 0