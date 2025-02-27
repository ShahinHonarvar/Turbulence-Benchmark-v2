def all_odd_ints_inclusive(int_list):
    output_list = []
    if len(int_list) > 0:
        if int_list[0] % 2 != 0:
            output_list.append(int_list[0])
    return output_list