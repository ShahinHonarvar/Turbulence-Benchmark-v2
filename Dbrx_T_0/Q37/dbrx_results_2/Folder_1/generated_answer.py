def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 41 or i > 79 or ord(input_string[i]) < ord('f') or (ord(input_string[i]) > ord('|')):
            filtered_string += input_string[i]
    return filtered_string