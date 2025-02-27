def insert_after_index(input_list):
    output_list = input_list[:]
    index = 93
    if index < len(output_list):
        output_list.insert(index + 1, [33, 78])
    else:
        output_list.append([33, 78])
    return output_list