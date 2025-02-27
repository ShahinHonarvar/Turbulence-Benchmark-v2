def all_neg_ints_inclusive(int_list):
    output = []
    for x in int_list[20:201]:
        if x < 0:
            output.append(x)
    return output