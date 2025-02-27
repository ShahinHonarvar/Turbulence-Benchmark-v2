def filter_chars(input_string: str) -> str:
    filtered_string = []
    to_remove = set()
    for char in input_string[344:875]:
        if 'f' < char < '~':
            to_remove.add(char)
    for char in input_string:
        if char not in to_remove:
            filtered_string.append(char)
    return ''.join(filtered_string)