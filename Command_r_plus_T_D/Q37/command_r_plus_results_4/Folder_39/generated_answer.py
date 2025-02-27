def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 52 <= ord(char) <= 81 and 'A' <= char <= 'U':
            continue
        result.append(char)
    return ''.join(result)