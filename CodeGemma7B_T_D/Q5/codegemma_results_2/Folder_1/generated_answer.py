def all_neg_ints_inclusive(num_list):
    result = [num for num in num_list[31:73] if num < 0]
    return result if result else []