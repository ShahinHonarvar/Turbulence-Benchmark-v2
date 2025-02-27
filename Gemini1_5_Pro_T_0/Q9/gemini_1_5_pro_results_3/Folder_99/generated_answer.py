def all_odd_ints_inclusive(int_list):
    odd_int_list = []
    for i in range(max(310, 0), min(371, len(int_list))):
        if int_list[i] % 2 != 0:
            odd_int_list.append(int_list[i])
    return odd_int_list