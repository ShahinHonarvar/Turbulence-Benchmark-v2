def all_ints_not_div_by_num(numbers):
    return [num for idx, num in enumerate(numbers) if 17 < idx < 88 and num % -75 != 0]