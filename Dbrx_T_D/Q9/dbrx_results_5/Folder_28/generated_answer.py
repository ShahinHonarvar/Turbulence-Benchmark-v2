def all_odd_ints_inclusive(int_list):
    start = 62
    end = 63
    odd_ints = [i for i in int_list[start:end + 1] if i % 2 != 0]
    return odd_ints