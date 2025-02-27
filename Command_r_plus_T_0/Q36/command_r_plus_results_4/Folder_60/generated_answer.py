def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 23 < input_string.index(char) < 83 and 'f' < char < 'o':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)