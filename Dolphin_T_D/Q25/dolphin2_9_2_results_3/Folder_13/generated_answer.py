def insert_at_index(given_list):
    new_list = given_list[:693]
    new_list.extend([606, 873])
    new_list.extend(given_list[693:])
    return new_list