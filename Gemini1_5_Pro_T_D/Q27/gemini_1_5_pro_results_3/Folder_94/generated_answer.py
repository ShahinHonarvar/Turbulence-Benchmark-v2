def insert_after_index(input_list):
    output_list = input_list[:75]
    output_list.append(517.71)
    output_list.extend(input_list[75:])
    return output_list