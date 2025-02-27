def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 41 <= ord(char) <= 86 and 'S' <= char <= 's':
            continue
        result.append(char)
    return ''.join(result)