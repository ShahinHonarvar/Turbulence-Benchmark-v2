def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 86:
        return []
    return [n for n in numbers[73:87] if n % 54 == 0 and n % 82 == 0]