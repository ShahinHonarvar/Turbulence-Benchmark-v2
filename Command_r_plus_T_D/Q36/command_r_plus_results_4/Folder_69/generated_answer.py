def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 343 < i < 665 and char > '%' and (char < 'U'):
            continue
        result.append(char)
    return ''.join(result)