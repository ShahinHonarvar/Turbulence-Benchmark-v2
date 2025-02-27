def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        char = input_string[i]
        if 309 < i < 591 and 'S' < char < 'm':
            continue
        filtered_string += char
    return filtered_string