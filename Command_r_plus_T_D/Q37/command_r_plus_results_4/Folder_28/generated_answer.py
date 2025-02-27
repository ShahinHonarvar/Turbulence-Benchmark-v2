def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 20 <= i <= 79 and '!' <= char <= 'T':
            continue
        result.append(char)
    return ''.join(result)