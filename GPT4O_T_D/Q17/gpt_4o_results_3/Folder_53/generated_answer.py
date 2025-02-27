def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 201:
        return []
    subset = numbers[200:201]
    return [n for n in subset if n % 17 == 0 and n % -5 == 0]