def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 86 < input_string.index(char) < 94 and 'E' < char < '~':
            continue
        result.append(char)
    return ''.join(result)