def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 46 <= ord(char) <= 85 and '-' <= char <= 'X':
            continue
        result.append(char)
    return ''.join(result)