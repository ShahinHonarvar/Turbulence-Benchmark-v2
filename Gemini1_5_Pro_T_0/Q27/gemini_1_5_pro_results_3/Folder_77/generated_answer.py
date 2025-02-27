def insert_after_index(input_list):
    output_list = input_list[:586]
    output_list.append(993.71)
    output_list.extend(input_list[586:])
    return output_list