def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 51 < i < 76 and '5' < char < 'f':
            continue
        result.append(char)
    return ''.join(result)