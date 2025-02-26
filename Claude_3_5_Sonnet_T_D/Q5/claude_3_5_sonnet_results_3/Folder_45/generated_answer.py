def all_neg_ints_inclusive(int_list):
    start = min(30, len(int_list))
    end = min(201, len(int_list))
    return [num for num in int_list[start:end] if num < 0]