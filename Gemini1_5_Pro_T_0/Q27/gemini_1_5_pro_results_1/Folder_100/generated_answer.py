def insert_after_index(input_list):
    output_list = input_list[0:74]
    output_list.append(418.88)
    output_list.extend(input_list[74:])
    return output_list