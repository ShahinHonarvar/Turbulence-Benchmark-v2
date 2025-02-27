def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 51 <= ord(char) <= 96 and 'X' <= char <= 'p':
            continue
        result.append(char)
    return ''.join(result)