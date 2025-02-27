def all_odd_ints_exclusive(input_list):
    output_list = []
    for i in range(1, 2):
        if input_list[i] % 2 != 0:
            output_list.append(input_list[i])
    return output_list