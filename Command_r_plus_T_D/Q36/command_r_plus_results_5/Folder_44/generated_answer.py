def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 18 < i < 64 and '3' < char < 'B':
            continue
        result.append(char)
    return ''.join(result)