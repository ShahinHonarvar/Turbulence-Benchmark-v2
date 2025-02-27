def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 14 < i < 75 and '9' < char < 'K':
            continue
        result.append(char)
    return ''.join(result)