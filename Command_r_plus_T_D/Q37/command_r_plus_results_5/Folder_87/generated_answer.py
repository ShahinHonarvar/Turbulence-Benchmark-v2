def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'W' <= char <= '[' and 18 <= i <= 81:
            continue
        result.append(char)
    return ''.join(result)