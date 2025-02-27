def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 45 < ord(char) < 57 and ord('F') < ord(char) < ord('n'):
            continue
        result.append(char)
    return ''.join(result)