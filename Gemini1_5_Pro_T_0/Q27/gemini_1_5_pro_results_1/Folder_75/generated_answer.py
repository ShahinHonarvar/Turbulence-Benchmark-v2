def insert_after_index(input_list):
    output_list = []
    index_of_99 = input_list.index(99)
    for i in range(len(input_list)):
        if i == index_of_99 + 1:
            output_list.append(99)
        output_list.append(input_list[i])
    return output_list