def insert_after_character(str_arg):
    processed_str = str_arg
    for character in processed_str:
        if character == 'P':
            processed_str += 'V'
    return processed_str