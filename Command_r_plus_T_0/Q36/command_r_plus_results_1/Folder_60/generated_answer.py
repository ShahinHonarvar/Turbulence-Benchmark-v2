def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 23 <= i < 83 and 'f' < char < 'o':
            continue
        result.append(char)
    return ''.join(result)