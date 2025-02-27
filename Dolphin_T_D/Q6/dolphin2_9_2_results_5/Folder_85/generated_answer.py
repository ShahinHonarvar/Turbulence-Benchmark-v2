def all_neg_ints_exclusive(input_list):
    negatives = []
    for i in range(5, len(input_list) - 4):
        if input_list[i] < 0:
            negatives.append(input_list[i])
    return negatives