def insert_after_index(current_list):
    if len(current_list) != 20:
        return current_list
    new_list = current_list[:19]
    new_list.append(742.2)
    new_list.extend(current_list[19:])
    return new_list