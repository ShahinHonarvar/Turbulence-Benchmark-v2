def filter_chars(s: str) -> str:
    result = ''
    for i in range(len(s)):
        if i < 12 or i > 25 or (s[i] < 'P' or s[i] > 'x'):
            result += s[i]
    return result