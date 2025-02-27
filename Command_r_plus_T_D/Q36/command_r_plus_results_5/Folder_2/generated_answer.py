def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 421 <= index < 854 and 'D' < char < 'J':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)