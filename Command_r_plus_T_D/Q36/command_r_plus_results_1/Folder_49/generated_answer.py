def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 46 < ord(char) < 91 and ord('D') < ord(char) < ord('H'):
            continue
        result.append(char)
    return ''.join(result)