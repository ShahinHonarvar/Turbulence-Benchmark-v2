def insert_at_index(input_list):
    if len(input_list) > 427:
        return input_list[:427] + [312, 441] + input_list[427:]
    else:
        return input_list + [0] * (427 - len(input_list)) + [312, 441]