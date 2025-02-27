def filter_chars(s: str) -> str:
    result = []
    for idx, char in enumerate(s):
        if 124 <= idx <= 854 and '9' <= char <= 's':
            continue
        result.append(char)
    return ''.join(result)