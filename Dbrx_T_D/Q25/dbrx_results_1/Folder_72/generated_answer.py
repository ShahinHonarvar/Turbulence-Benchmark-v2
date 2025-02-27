def insert_at_index(input_list):
    new_list = [98, 22]
    for i in range(24, len(input_list)):
        new_list.append(input_list[i])
    new_list.append(input_list[24])
    return new_list