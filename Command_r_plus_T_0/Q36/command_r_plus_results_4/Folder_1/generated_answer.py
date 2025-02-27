def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 69 < input_string.index(char) < 87 and '#' < char < 'L':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)