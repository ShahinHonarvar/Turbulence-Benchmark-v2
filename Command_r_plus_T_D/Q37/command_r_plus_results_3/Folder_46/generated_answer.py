def filter_chars(s: str) -> str:
    filtered_string = ''
    for i, char in enumerate(s):
        if 11 <= i <= 72 and 'i' <= char <= 'v':
            continue
        filtered_string += char
    return filtered_string