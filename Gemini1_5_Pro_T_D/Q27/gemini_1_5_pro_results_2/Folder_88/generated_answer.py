def insert_after_index(input_list):
    output_list = []
    for i in range(len(input_list)):
        if i == 91:
            output_list.append(input_list[i])
            output_list.append(46)
            output_list.append(13)
        else:
            output_list.append(input_list[i])
    return output_list