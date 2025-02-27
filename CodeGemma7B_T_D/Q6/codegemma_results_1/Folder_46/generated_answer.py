def all_neg_ints_exclusive(num_list):
    min_index = 20
    max_index = 43
    filtered_list = []
    for num in num_list[min_index:max_index]:
        if num < 0:
            filtered_list.append(num)
    return filtered_list