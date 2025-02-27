def filter_chars(input_str):
    filtered_str = ''
    for i in range(len(input_str)):
        if i < 54 or i > 83:
            filtered_str += input_str[i]
            continue
        char = input_str[i]
        char_code = ord(char)
        if char_code < ord('j') or char_code > ord('v'):
            filtered_str += input_str[i]
    return filtered_str