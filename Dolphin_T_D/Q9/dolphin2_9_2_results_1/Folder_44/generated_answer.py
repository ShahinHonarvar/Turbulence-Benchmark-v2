def all_odd_ints_inclusive(ints_list):
    result = [ints_list[i] for i in range(13, 69) if ints_list[i] % 2 != 0]
    return result