def remove_repeat_chars(s: str) -> str:
    for char in set(s[20:51]):
        if s[20:51].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s