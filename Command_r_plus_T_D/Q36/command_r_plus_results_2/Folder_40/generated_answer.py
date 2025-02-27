def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 1 < input_string.index(char) < 7 and ord(char) > ord('-') and (ord(char) < ord('L')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)