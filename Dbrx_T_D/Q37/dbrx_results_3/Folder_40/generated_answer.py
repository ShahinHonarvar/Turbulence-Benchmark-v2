def filter_chars(input_string):
    result = ''
    for char in input_string:
        if ord('*') <= ord(char) <= ord('s') and input_string.index(char) < 2:
            continue
        else:
            result += char
    return result