def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 81 < input_string.index(char) < 86 and '!' < char < 's':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)