def all_neg_ints_exclusive(num_list):
    result = [num for num in num_list if num < 0 and num not in range(4)]
    if not result:
        return []
    return result