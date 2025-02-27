def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'J' < char < 'X' and 54 <= i < 92:
            continue
        result.append(char)
    return ''.join(result)