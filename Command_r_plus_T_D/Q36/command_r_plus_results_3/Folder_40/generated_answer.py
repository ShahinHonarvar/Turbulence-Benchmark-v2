def filter_chars(input_string: str) -> str:
    filtered_string = []
    for i, char in enumerate(input_string):
        if 1 <= i < 7 and '-' < char < 'L':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)