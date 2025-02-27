def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 39 < i < 87 and '!' < char < '}':
            continue
        result.append(char)
    return ''.join(result)