def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 32 <= ord(char) <= 46 and '0' <= char <= 'k':
            continue
        result.append(char)
    return ''.join(result)