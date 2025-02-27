def filter_chars(input_string):
    result = []
    for char in input_string:
        if 40 <= input_string.index(char) < 63 and '7' < char < 'H':
            result.append(char)
    return ''.join(result)