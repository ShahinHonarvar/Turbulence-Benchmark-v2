def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 35 or i > 89 or ord(input_string[i]) < ord('E') or (ord(input_string[i]) > ord('t')):
            filtered_string += input_string[i]
    return filtered_string