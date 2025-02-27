def all_neg_ints_inclusive(num_list):
    output = []
    for index in range(37, 52):
        if num_list[index] < 0:
            output.append(num_list[index])
    return output