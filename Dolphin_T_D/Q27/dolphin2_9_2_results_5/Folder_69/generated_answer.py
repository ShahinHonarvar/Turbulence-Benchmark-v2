def insert_after_index(a_list):
    new_list = a_list[:564]
    new_list.append(149)
    new_list += a_list[564:]
    return new_list