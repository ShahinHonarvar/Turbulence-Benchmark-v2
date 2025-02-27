def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if '?' < char < 'k':
            if 3 <= input_string.index(char) < 8:
                continue
        filtered_string.append(char)
    return ''.join(filtered_string)