def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if 8 <= i <= 9:
            char = s[i]
            if 'R' <= char <= 't':
                s = s.replace(char, '', 1)
    return s