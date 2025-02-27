def remove_repeat_chars(s: str) -> str:
    for char in set(s[2:8]):
        if s[2:8].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s