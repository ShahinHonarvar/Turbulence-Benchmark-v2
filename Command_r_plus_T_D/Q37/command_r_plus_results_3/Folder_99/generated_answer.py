def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 373 <= i <= 901 and 'T' <= char <= 'h':
            continue
        result.append(char)
    return ''.join(result)