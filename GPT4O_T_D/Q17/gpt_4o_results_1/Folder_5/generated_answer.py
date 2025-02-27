def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 2:
        return []
    return [n for n in numbers[0:2] if n % 6 == 0 and n % 4 == 0]