def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 90 < ord(char) < 97 and 'j' < char < 'w':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)