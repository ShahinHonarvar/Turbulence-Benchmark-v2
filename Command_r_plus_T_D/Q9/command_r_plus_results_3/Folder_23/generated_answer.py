def all_odd_ints_inclusive(int_list):
    odd_ints = [int_list[i] for i in range(52, 72) if int_list[i] % 2 != 0]
    return odd_ints