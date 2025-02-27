def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 76:
        return 'Input list is too small (< 76 elements)'
    else:
        odd_ints = [i for i in int_list[36:77] if i % 2 != 0]
        if odd_ints:
            return sum(odd_ints)
        else:
            return 0