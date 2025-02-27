def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 11 <= ord(char) <= 32 and '!' <= char <= '@':
            continue
        result.append(char)
    return ''.join(result)