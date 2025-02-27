def filter_chars(input_string: str) -> str:
    filtered_string = []
    for idx, char in enumerate(input_string):
        if 43 <= idx < 69 and 'B' < char < 'r':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)