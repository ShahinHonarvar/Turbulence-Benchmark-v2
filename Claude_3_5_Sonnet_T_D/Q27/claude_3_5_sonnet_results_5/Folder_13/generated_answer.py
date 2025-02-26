def insert_after_index(input_list):
    try:
        index = input_list.index(693)
        return input_list[:index + 1] + [606, 873] + input_list[index + 1:]
    except ValueError:
        return input_list + [606, 873]