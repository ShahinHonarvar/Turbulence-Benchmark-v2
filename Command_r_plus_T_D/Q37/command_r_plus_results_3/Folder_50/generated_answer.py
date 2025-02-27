def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 71 <= ord(char) <= 96 and '_' <= char <= 'o':
            continue
        result.append(char)
    return ''.join(result)