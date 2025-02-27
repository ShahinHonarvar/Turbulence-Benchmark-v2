def insert_after_index(input_list):
    new_list = []
    for i, element in enumerate(input_list):
        if i == 52:
            new_list.append(element)
            new_list.append(38)
        else:
            new_list.append(element)
    return new_list