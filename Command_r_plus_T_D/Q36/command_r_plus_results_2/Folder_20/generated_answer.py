def filter_chars(input_string: str) -> str:
    filtered_string = []
    for idx, char in enumerate(input_string):
        if 13 <= idx < 40 and ':' < char < 'C':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)