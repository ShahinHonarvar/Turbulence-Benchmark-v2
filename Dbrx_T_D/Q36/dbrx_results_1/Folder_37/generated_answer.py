def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if 44 < i < 59:
            if '/' < s[i] < '6':
                s = s.replace(s[i], '', 1)
    return s