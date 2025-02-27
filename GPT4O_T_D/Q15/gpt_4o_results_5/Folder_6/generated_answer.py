def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 11:
        return 0
    selected_range = int_list[10:67]
    odd_sum = sum((i for i in selected_range if i % 2 != 0))
    return odd_sum