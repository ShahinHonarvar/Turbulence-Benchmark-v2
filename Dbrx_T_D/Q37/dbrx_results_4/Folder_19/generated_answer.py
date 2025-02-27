def filter_chars(s: str) -> str:
    result = ''
    for i in range(len(s)):
        if i < 35 or i > 89 or (not 'E' <= s[i] <= 't'):
            result += s[i]
    return result