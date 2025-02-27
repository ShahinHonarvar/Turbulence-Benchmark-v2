def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 259 or i > 502:
            filtered_string += input_string[i]
            continue
        char_code = ord(input_string[i])
        if char_code >= ord(',') and char_code <= ord('3'):
            continue
        filtered_string += input_string[i]
    return filtered_string