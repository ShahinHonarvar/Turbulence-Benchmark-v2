def all_odd_ints_exclusive(int_list):
    odd_numbers = []
    for i in range(598, 767):
        if int_list[i] % 2 != 0:
            odd_numbers.append(int_list[i])
    return odd_numbers