def all_neg_ints_exclusive(int_list):
    filtered_list = [num for num in int_list[2:7] if num < 0]
    return filtered_list if filtered_list != [] else []