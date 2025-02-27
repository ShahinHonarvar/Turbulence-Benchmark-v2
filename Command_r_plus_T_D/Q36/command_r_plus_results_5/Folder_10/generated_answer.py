def filter_chars(input_string: str) -> str:
    filtered_string = []
    for idx, char in enumerate(input_string, 1):
        if 35 < idx < 61 and '!' < char < 'B':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)