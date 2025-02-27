def all_ints_div_by_num(ints):
    div_by_num_ints = [ints[i] for i in range(10, 38) if ints[i] % -64 == 0]
    return div_by_num_ints