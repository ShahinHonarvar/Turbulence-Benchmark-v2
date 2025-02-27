def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 225 <= ord(char) <= 381 and 'D' <= char <= 'Y':
            continue
        result.append(char)
    return ''.join(result)