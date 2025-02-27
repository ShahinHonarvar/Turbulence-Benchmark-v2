def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 41 < input_string.index(char) < 56 and 'Z' < char < 'c':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)