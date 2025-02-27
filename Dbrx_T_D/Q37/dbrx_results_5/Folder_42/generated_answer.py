def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 73 or i > 74 or (ord(input_string[i]) < 85 and ord(input_string[i]) > 108):
            filtered_string += input_string[i]
    return filtered_string