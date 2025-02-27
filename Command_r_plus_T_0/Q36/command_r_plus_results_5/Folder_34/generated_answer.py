def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 10 <= i < 79 and '?' < char < 'm':
            continue
        result.append(char)
    return ''.join(result)