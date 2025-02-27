def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 27 <= ord(char) <= 85 and 'c' <= char <= 'i':
            continue
        result.append(char)
    return ''.join(result)