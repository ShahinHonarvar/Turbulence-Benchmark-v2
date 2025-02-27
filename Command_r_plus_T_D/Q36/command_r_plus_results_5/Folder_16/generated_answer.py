def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 331 < i < 713 and 'M' < char < '_':
            continue
        result.append(char)
    return ''.join(result)