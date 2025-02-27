def all_neg_ints_exclusive(num_list):
    result = []
    for num in num_list[43:99]:
        if num < 0:
            result.append(num)
    return result