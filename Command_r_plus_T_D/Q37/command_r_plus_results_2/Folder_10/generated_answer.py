def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 63 <= ord(char) <= 84 and 'E' <= char <= '~':
            continue
        result.append(char)
    return ''.join(result)