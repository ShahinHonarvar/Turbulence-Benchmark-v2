def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 722 <= s.index(char) <= 832 and 'K' <= char <= 'm':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)