def filter_chars(s: str) -> str:
    for i in range(18, 38):
        if ord(')') < ord(s[i]) < ord('P'):
            s = s.replace(s[i], '')
    return s