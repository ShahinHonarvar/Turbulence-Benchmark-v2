def all_odd_ints_inclusive(list):
    output_list = []
    for i in range(22, 51):
        if list[i] % 2 != 0:
            output_list.append(list[i])
    return output_list