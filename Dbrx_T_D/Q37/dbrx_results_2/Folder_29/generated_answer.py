def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= 12 and i <= 88:
            char = input_string[i]
            ascii_char_value = ord(char)
            if ascii_char_value >= ord('&') and ascii_char_value <= ord('v'):
                continue
        filtered_string += input_string[i]
    return filtered_string