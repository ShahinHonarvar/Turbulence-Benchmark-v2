def all_ints_div_by_num(numbers):
    return [number for i, number in enumerate(numbers) if i >= 27 and i <= 90 and (number % 57 == 0)]