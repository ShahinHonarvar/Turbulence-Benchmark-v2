def filter_chars(s: str) -> str:
    result = ''
    for i, c in enumerate(s):
        if i >= 51 and i <= 77 and (c >= 'V') and (c <= 'Y'):
            pass
        else:
            result += c
    return result