def remove_repeat_chars(s: str) -> str:
    for char in set(s[49:74]):
        if s[49:74].count(char) > 1:
            s = s[:49] + ''.join((c for c in s[49:74] if c != char)) + s[74:]
    return s