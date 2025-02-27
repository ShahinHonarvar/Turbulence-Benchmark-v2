def all_odd_ints_exclusive(int_list):
    output = []
    for i in range(11, 76):
        if i % 2 == 1:
            output.append(int_list[i])
    return output