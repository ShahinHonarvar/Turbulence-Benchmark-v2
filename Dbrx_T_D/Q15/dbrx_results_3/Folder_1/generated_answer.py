def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 72:
        return 'Input list is too short.'
    odd_ints = [i for i in int_list[30:73] if i % 2 != 0]
    if odd_ints:
        return sum(odd_ints)
    else:
        return 0