def all_neg_ints_exclusive(num_list):
    result = []
    for i in range(1, 8):
        if -i in num_list:
            result.append(-i)
    return result