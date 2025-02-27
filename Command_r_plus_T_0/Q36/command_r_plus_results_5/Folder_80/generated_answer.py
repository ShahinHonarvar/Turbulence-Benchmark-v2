def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 54 < input_string.index(char) < 92 and 'J' < char < 'X':
            continue
        result.append(char)
    return ''.join(result)