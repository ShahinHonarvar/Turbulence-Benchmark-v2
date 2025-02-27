def insert_after_index(input_list):
    i = 0
    while i < len(input_list):
        if input_list[i] == 99:
            input_list.insert(i + 1, 99)
            break
        i += 1
    return input_list