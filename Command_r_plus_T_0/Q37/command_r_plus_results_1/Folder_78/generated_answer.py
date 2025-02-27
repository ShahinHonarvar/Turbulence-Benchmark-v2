def filter_chars(s: str) -> str:
    filtered_string = ''
    for index, char in enumerate(s):
        if 75 <= index <= 99 and '8' <= char <= 'e':
            continue
        filtered_string += char
    return filtered_string