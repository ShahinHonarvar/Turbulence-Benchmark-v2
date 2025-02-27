def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'E' <= char <= 't' and 35 <= i <= 89:
            continue
        result.append(char)
    return ''.join(result)