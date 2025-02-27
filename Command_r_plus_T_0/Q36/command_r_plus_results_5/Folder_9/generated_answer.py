def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 50 < input_string.index(char) < 92 and 'A' < char < 'Q':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)