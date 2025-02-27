def insert_after_index(input_list):
    try:
        index = input_list.index(43) + 1
        return input_list[:index] + [37] + input_list[index:]
    except ValueError:
        return input_list + [37]