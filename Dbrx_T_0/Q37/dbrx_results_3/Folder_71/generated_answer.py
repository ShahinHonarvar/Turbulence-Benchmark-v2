def filter_chars(input_string):
    result = ''
    for char in input_string:
        if not (32 <= ord(char) <= 46 and '0' <= char <= 'k'):
            result += char
    return result