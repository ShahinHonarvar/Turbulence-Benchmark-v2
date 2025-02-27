def filter_chars(input_string: str) -> str:
    filtered_string = []
    for idx, char in enumerate(input_string):
        if 42 <= idx < 68 and 't' < char < 'x':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)