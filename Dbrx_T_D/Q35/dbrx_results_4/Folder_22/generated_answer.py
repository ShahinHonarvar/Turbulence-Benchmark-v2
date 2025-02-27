def remove_repeat_chars(s: str) -> str:
    for char in set(s[50:200]):
        if s[50:200].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s