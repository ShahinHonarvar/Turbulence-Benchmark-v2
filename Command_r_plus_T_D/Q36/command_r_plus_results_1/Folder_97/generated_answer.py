def filter_chars(input_string: str) -> str:
    filtered_string = []
    to_remove = set()
    for char_idx, char in enumerate(input_string):
        if 309 <= char_idx < 591 and 'S' < char < 'm':
            to_remove.add(char)
    for char in input_string:
        if char not in to_remove:
            filtered_string.append(char)
    return ''.join(filtered_string)