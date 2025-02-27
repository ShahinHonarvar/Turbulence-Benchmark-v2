def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in int_list[14:65]:
        if i % 2 != 0:
            odd_ints.append(i)
    return odd_ints