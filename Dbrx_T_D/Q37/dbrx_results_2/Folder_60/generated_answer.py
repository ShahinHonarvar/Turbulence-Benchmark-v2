def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 12 or i > 77 or ord(input_string[i]) < ord(':') or (ord(input_string[i]) > ord('L')):
            filtered_string += input_string[i]
    return filtered_string