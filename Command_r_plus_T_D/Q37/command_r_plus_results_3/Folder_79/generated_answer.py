def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 10 <= ord(char) <= 52 and '@' <= char <= 'T':
            continue
        result.append(char)
    return ''.join(result)