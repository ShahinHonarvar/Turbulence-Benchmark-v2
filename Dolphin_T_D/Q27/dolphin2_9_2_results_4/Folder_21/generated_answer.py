def insert_after_index(data_list):
    new_list = data_list[:744]
    new_list.append(11.04)
    new_list.extend(data_list[744:])
    return new_list