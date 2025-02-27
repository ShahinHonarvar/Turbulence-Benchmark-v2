def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if not (29 <= i <= 79 and 'K' <= char <= 'z'):
            result.append(char)
    return ''.join(result)