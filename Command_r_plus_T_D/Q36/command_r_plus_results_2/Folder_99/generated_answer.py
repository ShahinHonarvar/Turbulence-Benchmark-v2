def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 476 < i < 948 and 'b' < char < 'd':
            continue
        result.append(char)
    return ''.join(result)