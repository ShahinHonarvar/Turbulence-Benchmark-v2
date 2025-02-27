def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not '-' < c < 'v']
    result = list(s)
    for i in range(221, 419):
        if s[i] in filtered_chars:
            result[i] = ''
    return ''.join(result)