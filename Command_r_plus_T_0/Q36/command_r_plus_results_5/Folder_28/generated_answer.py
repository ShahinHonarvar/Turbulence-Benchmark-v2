def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 31 < ord(char) < 73 and char > 'M' and (char < 'j'):
            continue
        result.append(char)
    return ''.join(result)