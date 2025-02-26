def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 95:
        return 0
    return sum((num for num in integer_list[75:95] if num % 2 != 0))