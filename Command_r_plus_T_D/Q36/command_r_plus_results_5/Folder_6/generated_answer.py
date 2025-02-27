def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 31 < ord(char) < 70 and ord('B') < ord(char) < ord('v'):
            continue
        result.append(char)
    return ''.join(result)