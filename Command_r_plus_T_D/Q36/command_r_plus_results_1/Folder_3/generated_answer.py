def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 42 <= i < 78 and '!' < char < '?':
            continue
        result.append(char)
    return ''.join(result)