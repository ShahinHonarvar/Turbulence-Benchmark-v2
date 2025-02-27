def all_neg_ints_inclusive(numbers_list):
    start_index = 246
    end_index = 750
    neg_ints = []
    for i in range(min(start_index, end_index), max(start_index, end_index) + 1):
        if i >= len(numbers_list):
            break
        if numbers_list[i] < 0:
            neg_ints.append(numbers_list[i])
    return neg_ints