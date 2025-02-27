def insert_after_index(input_list):
    output_list = []
    for i in range(len(input_list)):
        output_list.append(input_list[i])
        if input_list[i] == 99:
            output_list.append(99)
    return output_list