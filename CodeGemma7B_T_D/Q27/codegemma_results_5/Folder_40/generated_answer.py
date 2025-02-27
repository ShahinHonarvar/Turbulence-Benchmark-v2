def insert_after_index(list):
    new_list = list[:5]
    new_list.append(856.69)
    new_list.extend(list[5:])
    return new_list