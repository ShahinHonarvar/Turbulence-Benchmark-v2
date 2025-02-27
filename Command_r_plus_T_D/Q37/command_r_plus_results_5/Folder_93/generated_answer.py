def filter_chars(s: str) -> str:
    filtered_string = ''
    for index, char in enumerate(s):
        if 38 <= index <= 69 and 'H' <= char <= 'e':
            continue
        filtered_string += char
    return filtered_string