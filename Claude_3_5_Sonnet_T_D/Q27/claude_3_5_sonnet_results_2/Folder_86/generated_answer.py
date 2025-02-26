def insert_after_index(input_list):
    try:
        index = input_list.index(990)
        return input_list[:index + 1] + [905, 742] + input_list[index + 1:]
    except ValueError:
        return input_list + [905, 742]