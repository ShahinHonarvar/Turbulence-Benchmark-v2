def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 27 <= ord(char) <= 85 and '!' <= char <= 'B':
            continue
        result.append(char)
    return ''.join(result)