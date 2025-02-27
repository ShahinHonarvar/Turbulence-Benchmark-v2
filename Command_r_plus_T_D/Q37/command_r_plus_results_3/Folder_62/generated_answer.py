def filter_chars(s: str) -> str:
    filtered_string = ''
    for index, char in enumerate(s):
        if 10 <= index <= 69 and 'I' <= char <= 'K':
            continue
        filtered_string += char
    return filtered_string