def all_ints_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i >= 10 and i <= 52 and (num % 12 == 0)]