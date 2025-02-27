def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 19 <= ord(char) <= 90 and 'F' <= char <= 'h':
            continue
        result.append(char)
    return ''.join(result)