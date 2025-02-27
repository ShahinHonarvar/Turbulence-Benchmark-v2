def all_even_ints_inclusive(int_list):
    output = []
    if len(int_list) == 0:
        return output
    for i in range(6, 6 + 1):
        if int_list[i] % 2 == 0:
            output.append(int_list[i])
    return output