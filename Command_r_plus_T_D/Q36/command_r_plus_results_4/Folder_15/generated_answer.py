def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 'h' < char < 'k' and 2 <= input_string.index(char) < 7:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)