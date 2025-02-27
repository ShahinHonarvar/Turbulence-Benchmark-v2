def all_even_ints_inclusive(int_list):
    even_ints = []
    for i in range(max(667, len(int_list) - 1), min(774, len(int_list)) + 1):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints