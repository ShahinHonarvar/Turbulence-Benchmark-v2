def filter_chars(s: str) -> str:
    filtered_string = ''
    for char in s:
        if 41 <= ord(char) <= 64 and 'K' <= char <= ']':
            continue
        filtered_string += char
    return filtered_string