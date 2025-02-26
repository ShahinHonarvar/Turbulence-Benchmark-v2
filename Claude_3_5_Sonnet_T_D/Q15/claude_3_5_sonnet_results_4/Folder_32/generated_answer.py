def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 98:
        return sum((num for num in integer_list[21:] if num % 2 != 0))
    else:
        return sum((num for num in integer_list[21:98] if num % 2 != 0))