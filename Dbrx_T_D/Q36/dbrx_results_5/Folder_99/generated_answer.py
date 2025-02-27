def filter_chars(s: str) -> str:
    result = ''
    for i in range(len(s)):
        if not (i >= 476 and i < 948 and (s[i] > 'b') and (s[i] < 'd')):
            result += s[i]
    return result