def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if '5' <= char < '9':
            continue
        result.append(char)
    return ''.join(result)