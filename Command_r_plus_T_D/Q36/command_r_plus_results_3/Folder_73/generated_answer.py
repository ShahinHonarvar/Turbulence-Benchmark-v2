def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 66 < ord(char) < 90 and '#' < char < 'T':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)