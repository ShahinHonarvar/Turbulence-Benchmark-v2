def filter_chars(input_string):
    result = ''
    for i, char in enumerate(input_string):
        if 38 <= i <= 54 and ':' <= char <= 'r':
            result += input_string.replace(char, '')
            break
        result += char
    return result