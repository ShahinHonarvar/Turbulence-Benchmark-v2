def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 138 <= i <= 920 and '6' <= char <= 'A':
            continue
        result.append(char)
    return ''.join(result)