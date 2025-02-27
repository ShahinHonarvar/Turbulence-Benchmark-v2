def filter_chars(input_string: str) -> str:
    filtered_string = []
    for idx, char in enumerate(input_string):
        if 55 <= idx < 80 and 'S' < char < 's':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)