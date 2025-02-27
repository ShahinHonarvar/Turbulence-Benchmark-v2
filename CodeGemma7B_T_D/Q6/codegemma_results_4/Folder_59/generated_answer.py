def all_neg_ints_exclusive(num_list):
    if not any((num < 0 for num in num_list)):
        return []
    return [num for num in num_list[0:10] if num < 0 and num not in range(1, 10)]