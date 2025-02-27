def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 42 or i > 97 or ord(input_string[i]) < ord('*') or (ord(input_string[i]) > ord('b')):
            filtered_string += input_string[i]
    return filtered_string