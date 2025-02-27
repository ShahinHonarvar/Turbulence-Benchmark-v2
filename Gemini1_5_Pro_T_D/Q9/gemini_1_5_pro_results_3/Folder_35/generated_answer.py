def all_odd_ints_inclusive(input_list):
    output_list = []
    for i in range(30, 49):
        if i < len(input_list) and input_list[i] % 2 != 0:
            output_list.append(input_list[i])
    return output_list