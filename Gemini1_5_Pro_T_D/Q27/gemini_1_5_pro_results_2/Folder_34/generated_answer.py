def insert_after_index(input_list):
    output_list = input_list[:54]
    output_list.append(783.25)
    output_list.extend(input_list[54:])
    return output_list