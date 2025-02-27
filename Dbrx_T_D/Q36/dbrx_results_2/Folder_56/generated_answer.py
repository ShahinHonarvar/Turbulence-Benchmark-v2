def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if 31 < i < 50:
            char = s[i]
            if '/' < char < 'J':
                s = s.replace(char, '', 1)
    return s