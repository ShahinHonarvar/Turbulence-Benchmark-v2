def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 20 or i > 79 or (i >= 20 and i <= 79 and (ord(input_string[i]) < ord('!')) or ord(input_string[i]) > ord('T')):
            filtered_string += input_string[i]
    return filtered_string