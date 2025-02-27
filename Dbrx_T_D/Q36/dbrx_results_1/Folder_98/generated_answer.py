def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if 4 < i < 8:
            char = s[i]
            if ord('1') < ord(char) < ord('J'):
                s = s.replace(char, '', 1)
    return s