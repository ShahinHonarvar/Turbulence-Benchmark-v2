def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 31 < ord(char) < 50 and ord(char) > ord('/') and (ord(char) < ord('J')):
            continue
        result.append(char)
    return ''.join(result)