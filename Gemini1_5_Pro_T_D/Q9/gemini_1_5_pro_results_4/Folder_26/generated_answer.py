def all_odd_ints_inclusive(input_list):
    output_list = []
    for i in range(max(0, min(62, len(input_list))), min(100, len(input_list))):
        if input_list[i] % 2 != 0:
            output_list.append(input_list[i])
    return output_list