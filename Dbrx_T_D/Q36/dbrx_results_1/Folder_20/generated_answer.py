def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if s[i] > ':' and s[i] < 'C' and (13 < i < 40):
            s = s.replace(s[i], '')
    return s