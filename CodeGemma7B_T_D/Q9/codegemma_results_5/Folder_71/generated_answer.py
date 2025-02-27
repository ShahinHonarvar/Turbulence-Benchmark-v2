def all_odd_ints_inclusive(input_list):
    output = []
    for i in range(26, 53):
        if i % 2 != 0:
            output.append(input_list[i])
    return output