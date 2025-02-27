def insert_after_index(input_list):
    output_list = []
    index_of_99 = -1
    for i, element in enumerate(input_list):
        if element == 99:
            index_of_99 = i
    if index_of_99 == -1:
        return input_list
    else:
        for i in range(len(input_list) + 1):
            if i < index_of_99 + 1:
                output_list.append(input_list[i])
            elif i == index_of_99 + 1:
                output_list.append(99)
            else:
                output_list.append(input_list[i - 1])
        return output_list