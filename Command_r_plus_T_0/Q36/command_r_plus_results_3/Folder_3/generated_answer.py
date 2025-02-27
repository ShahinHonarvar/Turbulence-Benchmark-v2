def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 42 < input_string.index(char) < 78 and '!' < char < '?':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)