def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        char = input_string[i]
        if (i >= 38 and i <= 69) and ord('H') <= ord(char) <= ord('e'):
            continue
        else:
            filtered_string += char
    return filtered_string