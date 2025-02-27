def all_odd_ints_inclusive(integer_list):
    start_index = 56
    end_index = 66
    odd_ints = [i for i in integer_list[start_index:end_index + 1] if i % 2 != 0]
    return odd_ints