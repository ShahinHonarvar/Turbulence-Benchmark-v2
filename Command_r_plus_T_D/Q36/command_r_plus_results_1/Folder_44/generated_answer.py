def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 18 < input_string.index(char) < 64 and '3' < char < 'B':
            continue
        result.append(char)
    return ''.join(result)