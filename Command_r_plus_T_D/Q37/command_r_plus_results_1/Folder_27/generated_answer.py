def filter_chars(s: str) -> str:
    filtered_string = ''
    for char in s:
        if 43 <= s.index(char) <= 80 and '=' <= char <= 'E':
            continue
        filtered_string += char
    return filtered_string