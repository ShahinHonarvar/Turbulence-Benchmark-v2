def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 83 or i > 99 or ord(input_string[i]) < ord('*') or (ord(input_string[i]) > ord('j')):
            filtered_string += input_string[i]
    return filtered_string