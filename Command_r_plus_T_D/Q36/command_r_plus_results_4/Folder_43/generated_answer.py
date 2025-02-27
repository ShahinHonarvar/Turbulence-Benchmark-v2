def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 27 < input_string.index(char) < 75 and 'A' < char < 'i':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)