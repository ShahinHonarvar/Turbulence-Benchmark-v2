def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'I' <= char <= 'K' and 10 <= i <= 69:
            continue
        result.append(char)
    return ''.join(result)