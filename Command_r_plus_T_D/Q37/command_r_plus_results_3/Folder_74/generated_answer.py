def filter_chars(s: str) -> str:
    filtered_string = ''
    for char in s:
        if 19 <= s.index(char) <= 32 and 'f' <= char <= 'o':
            continue
        filtered_string += char
    return filtered_string