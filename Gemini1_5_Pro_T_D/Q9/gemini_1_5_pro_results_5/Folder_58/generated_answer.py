def all_odd_ints_inclusive(input_list):
    output_list = []
    for i in range(max(209, 0), min(len(input_list), 557)):
        if input_list[i] % 2 != 0:
            output_list.append(input_list[i])
    return output_list