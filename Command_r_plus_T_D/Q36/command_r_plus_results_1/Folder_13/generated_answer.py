def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 323 < input_string.index(char) < 526 and ')' < char < 'O':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)