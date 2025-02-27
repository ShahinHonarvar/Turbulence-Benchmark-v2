def filter_chars(input_string: str) -> str:
    filtered_string = []
    remove_chars = []
    for char in input_string:
        if 669 < input_string.index(char) < 888 and 'B' < char < 'Y':
            remove_chars.append(char)
        else:
            filtered_string.append(char)
    for char in remove_chars:
        while char in filtered_string:
            filtered_string.remove(char)
    return ''.join(filtered_string)