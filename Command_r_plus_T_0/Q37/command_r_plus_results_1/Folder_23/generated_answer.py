def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 51 <= s.index(char) <= 77 and 'V' <= char <= 'Y':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)