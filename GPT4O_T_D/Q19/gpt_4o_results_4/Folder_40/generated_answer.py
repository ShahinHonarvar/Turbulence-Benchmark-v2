def all_ints_not_div_by_num(numbers):
    if len(numbers) < 3:
        return []
    return [n for n in numbers[1:2] if n % numbers[0] != 0]