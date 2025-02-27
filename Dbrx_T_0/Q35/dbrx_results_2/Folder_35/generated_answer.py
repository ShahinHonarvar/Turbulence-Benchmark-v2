def remove_repeat_chars(s: str) -> str:
    for char in set(s[77:84]):
        if s[77:84].count(char) > 1:
            s = s[:77] + s[77:84].replace(char, '', s[77:84].count(char) - 1) + s[84:]
    return s