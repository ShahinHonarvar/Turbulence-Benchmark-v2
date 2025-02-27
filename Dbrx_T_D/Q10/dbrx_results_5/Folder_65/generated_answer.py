def all_odd_ints_exclusive(int_list):
    start = 42
    end = 87
    odd_ints = [i for i in int_list[start:end] if i % 2 != 0]
    return odd_ints