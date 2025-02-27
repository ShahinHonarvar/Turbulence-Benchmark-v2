def filter_chars(input_string):
    result = ''
    for char in input_string:
        char_code = ord(char)
        if not (32 <= char_code <= 46 and '0' <= char <= 'k'):
            result += char
    return result