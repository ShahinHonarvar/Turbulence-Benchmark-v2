def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 19 <= i <= 92 and '8' <= char <= 'm':
            continue
        result.append(char)
    return ''.join(result)