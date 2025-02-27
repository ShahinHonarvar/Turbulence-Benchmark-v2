def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if (i < 42 or i > 92) or (ord(input_string[i]) < 47 or ord(input_string[i]) > 97):
            filtered_string += input_string[i]
    return filtered_string