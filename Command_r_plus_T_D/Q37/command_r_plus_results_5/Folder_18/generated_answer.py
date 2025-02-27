def filter_chars(input_string: str) -> str:
    filtered_string = []
    remove_chars = set()
    for index, char in enumerate(input_string[770:971], 770):
        if '-' <= char <= 'D':
            remove_chars.add(char)
    for char in input_string:
        if char not in remove_chars:
            filtered_string.append(char)
    return ''.join(filtered_string)