def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 56 <= i < 86 and '+' < char < 'w':
            continue
        result.append(char)
    return ''.join(result)