def all_odd_ints_inclusive(input_list):
    output_list = []
    for i in range(20, 201):
        if i >= len(input_list):
            break
        if input_list[i] % 2 != 0:
            output_list.append(input_list[i])
    return output_list