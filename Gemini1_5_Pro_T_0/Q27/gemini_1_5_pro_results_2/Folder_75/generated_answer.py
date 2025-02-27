def insert_after_index(input_list):
    output_list = []
    index_of_interest = None
    for i, element in enumerate(input_list):
        if element == 99:
            index_of_interest = i
    if index_of_interest is not None:
        for i in range(index_of_interest + 1):
            output_list.append(input_list[i])
        output_list.append(99)
        for i in range(index_of_interest + 1, len(input_list)):
            output_list.append(input_list[i])
    else:
        output_list = input_list
    return output_list