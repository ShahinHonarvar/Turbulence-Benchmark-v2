def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 477 or i > 984 or ord(input_string[i]) < ord(',') or (ord(input_string[i]) > ord('V')):
            filtered_string += input_string[i]
    return filtered_string