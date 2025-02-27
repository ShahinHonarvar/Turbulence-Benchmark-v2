def sum_odd_ints_inclusive(integer_list):
    if not integer_list or max(integer_list) < 0:
        return 0
    else:
        return sum((i for i in integer_list[0:1] if i % 2 != 0))