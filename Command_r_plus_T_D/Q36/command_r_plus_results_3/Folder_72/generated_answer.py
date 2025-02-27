def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'W' < char < 'x' and 44 <= i < 68:
            continue
        result.append(char)
    return ''.join(result)