def insert_after_index(input_list):
    output_list = []
    for i in range(len(input_list)):
        output_list.append(input_list[i])
        if i == 62:
            output_list.append(51)
    return output_list