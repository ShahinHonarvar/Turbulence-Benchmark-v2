def filter_chars(input_string: str) -> str:
    filtered_string = []
    for idx, char in enumerate(input_string):
        if 86 <= idx < 93 and 'E' < char < '~':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)