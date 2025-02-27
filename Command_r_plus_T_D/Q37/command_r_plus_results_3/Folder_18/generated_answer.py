def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 770 <= index <= 970 and '-' <= char <= 'D':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)