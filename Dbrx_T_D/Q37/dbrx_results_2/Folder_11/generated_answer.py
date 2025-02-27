def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 29 or i > 97:
            filtered_string += input_string[i]
            continue
        char = input_string[i]
        ascii_code = ord(char)
        if ascii_code >= ord('-') and ascii_code <= ord('n'):
            continue
        filtered_string += char
    return filtered_string