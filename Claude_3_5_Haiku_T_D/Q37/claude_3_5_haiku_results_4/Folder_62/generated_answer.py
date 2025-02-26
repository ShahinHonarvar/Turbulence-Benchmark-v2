def filter_chars(input_string):
    result = []
    for index, char in enumerate(input_string):
        if 10 <= index <= 69 and 'I' <= char <= 'K':
            continue
        result.append(char)
    return ''.join(result)