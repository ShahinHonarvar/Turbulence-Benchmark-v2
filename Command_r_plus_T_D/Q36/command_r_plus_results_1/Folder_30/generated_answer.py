def filter_chars(s: str) -> str:
    result = list(s)
    for i in range(23, 45):
        if '3' < s[i] < 'I':
            result.remove(s[i])
    return ''.join(result)