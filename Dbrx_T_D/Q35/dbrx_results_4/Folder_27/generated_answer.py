def remove_repeat_chars(s: str) -> str:
    for char in set(s[86:89]):
        if s[86:89].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s