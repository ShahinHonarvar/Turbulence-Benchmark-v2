def insert_after_index(input_list):
    output_list = []
    for i in range(len(input_list)):
        output_list.append(input_list[i])
        if i == 295:
            output_list.append(276)
            output_list.append(376)
    return output_list