def all_ints_div_by_both_two_nums(data):
    try:
        return [num for num in data[29:54] if num % -68 == 0 and num % -85 == 0]
    except IndexError:
        return []