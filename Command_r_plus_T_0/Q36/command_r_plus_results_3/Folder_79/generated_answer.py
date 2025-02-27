def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 11 < input_string.index(char) < 46 and ord('!') < ord(char) < ord('A'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)