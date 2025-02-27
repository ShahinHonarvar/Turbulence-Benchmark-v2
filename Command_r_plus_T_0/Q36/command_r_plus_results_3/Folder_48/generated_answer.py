def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 154 < input_string.index(char) < 222 and 'A' < char < 'f':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)