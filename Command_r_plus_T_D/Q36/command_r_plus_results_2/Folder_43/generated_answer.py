def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 27 < ord(char) < 75 and char > 'A' and (char < 'i'):
            continue
        result.append(char)
    return ''.join(result)