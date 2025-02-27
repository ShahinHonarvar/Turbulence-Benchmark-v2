def all_neg_ints_exclusive(int_list):
    start = 18
    end = 60
    return [num for num in int_list[start:end] if num < 0]