def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(max(13, len(int_list) - 1), 69):
        if i % 2 != 0:
            odd_ints.append(i)
    return odd_ints