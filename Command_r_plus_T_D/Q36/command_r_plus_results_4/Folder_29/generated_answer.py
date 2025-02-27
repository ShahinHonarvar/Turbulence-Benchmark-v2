def filter_chars(input_string: str) -> str:
    result = []
    for char in input_string:
        if 46 < input_string.index(char) < 68 and 'H' < char < 's':
            continue
        result.append(char)
    return ''.join(result)