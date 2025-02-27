def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 40 <= i < 63 and '7' < char < 'H':
            continue
        result.append(char)
    return ''.join(result)