def filter_chars(input_string: str) -> str:
    filtered_string = []
    to_remove = set()
    for index, char in enumerate(input_string):
        if 344 < index < 874 and 'f' < char < '~':
            to_remove.add(char)
    for char in input_string:
        if char not in to_remove:
            filtered_string.append(char)
    return ''.join(filtered_string)