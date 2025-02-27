def all_pos_ints_inclusive(input_list):
    output_list = []
    for n in input_list[1:9]:
        if n > 0:
            output_list.append(n)
    return output_list