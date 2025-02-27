def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i > 0 and i < 8 and (num % -3 != 0)]