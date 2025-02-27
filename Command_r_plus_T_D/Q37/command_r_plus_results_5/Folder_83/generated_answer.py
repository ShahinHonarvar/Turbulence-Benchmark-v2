def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 29 <= s.index(char) <= 79 and 'K' <= char <= 'z':
            continue
        result.append(char)
    return ''.join(result)