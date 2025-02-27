def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 63 or i > 84 or ord(input_string[i]) < ord('E') or (ord(input_string[i]) > ord('~')):
            filtered_string += input_string[i]
    return filtered_string