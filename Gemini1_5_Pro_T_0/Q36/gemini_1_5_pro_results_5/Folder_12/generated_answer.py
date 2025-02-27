def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        char = input_string[i]
        if 32 < i < 84 and 'm' < char < 'w':
            filtered_string += ''
        else:
            filtered_string += char
    return filtered_string