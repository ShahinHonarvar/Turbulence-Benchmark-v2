def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char_idx, char in enumerate(input_string):
        if 502 <= char_idx < 946 and 'W' < char < 'y':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)