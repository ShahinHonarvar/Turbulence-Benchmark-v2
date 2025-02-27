def filter_chars(s: str) -> str:
    result = ''
    for i in range(len(s)):
        if i < 36 or i > 79 or s[i] < '2' or (s[i] > 's'):
            result += s[i]
    return result