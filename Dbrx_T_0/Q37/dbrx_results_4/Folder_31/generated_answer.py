def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 57 or i > 96 or ord(input_string[i]) < ord('<') or (ord(input_string[i]) > ord('w')):
            filtered_string += input_string[i]
    return filtered_string