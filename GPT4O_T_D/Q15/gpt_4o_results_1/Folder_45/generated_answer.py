def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 31:
        return 0
    odd_sum = sum((i for i in int_list[30:201] if i % 2 != 0))
    return odd_sum