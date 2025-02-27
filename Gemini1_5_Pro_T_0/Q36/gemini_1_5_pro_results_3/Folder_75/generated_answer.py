def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        char = input_string[i]
        if 46 < i < 74 and '&' < char < 'M':
            filtered_string = filtered_string.replace(char, '')
        else:
            filtered_string += char
    return filtered_string