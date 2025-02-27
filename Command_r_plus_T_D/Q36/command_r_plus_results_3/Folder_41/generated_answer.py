def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 81 <= i < 89 and 'f' < char < '{':
            continue
        result.append(char)
    return ''.join(result)