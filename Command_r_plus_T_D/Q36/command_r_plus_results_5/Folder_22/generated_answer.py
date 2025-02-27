def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 55 < input_string.index(char) < 84 and char > ';' and (char < 'z'):
            continue
        result.append(char)
    return ''.join(result)