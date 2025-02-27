def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 23 < i < 45 and '3' < char < 'I':
            continue
        result.append(char)
    return ''.join(result)