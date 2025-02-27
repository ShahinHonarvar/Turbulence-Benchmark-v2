def insert_after_index(input_list):
    output_list = []
    for i in range(len(input_list)):
        if i == 55:
            output_list.append(input_list[i])
            output_list.append(26)
            output_list.append(10)
        else:
            output_list.append(input_list[i])
    return output_list