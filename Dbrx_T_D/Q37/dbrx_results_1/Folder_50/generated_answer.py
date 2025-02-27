def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 71 or i > 96 or ord(input_string[i]) < ord('_') or (ord(input_string[i]) > ord('o')):
            filtered_string += input_string[i]
    return filtered_string