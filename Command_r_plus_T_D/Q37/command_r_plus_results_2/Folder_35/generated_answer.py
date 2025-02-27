def filter_chars(s: str) -> str:
    filtered_string = ''
    for char in s:
        if 155 <= s.index(char) <= 403 and '(' <= char <= ']':
            continue
        filtered_string += char
    return filtered_string