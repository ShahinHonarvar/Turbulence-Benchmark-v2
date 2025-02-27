def filter_chars(input_string):
    result = ''
    for char in input_string:
        if not (ord(char) >= 57 and ord(char) <= 96 and (char >= '<') and (char <= 'w')):
            result += char
    return result