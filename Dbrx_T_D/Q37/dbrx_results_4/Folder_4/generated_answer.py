def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 19 or i > 33 or ord(input_string[i]) < ord('S') or (ord(input_string[i]) > ord('{')):
            filtered_string += input_string[i]
    return filtered_string