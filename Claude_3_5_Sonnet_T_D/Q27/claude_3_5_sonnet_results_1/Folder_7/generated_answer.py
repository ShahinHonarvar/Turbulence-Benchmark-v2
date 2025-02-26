def insert_after_index(input_list):
    try:
        index = input_list.index(323)
        return input_list[:index + 1] + [389, 303] + input_list[index + 1:]
    except ValueError:
        return input_list + [389, 303]