def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 1 <= i < 9 and '8' < char < 'm':
            continue
        result.append(char)
    return ''.join(result)