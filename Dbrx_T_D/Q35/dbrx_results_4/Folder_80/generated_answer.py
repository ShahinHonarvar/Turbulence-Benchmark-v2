def remove_repeat_chars(s: str) -> str:
    char_count = {c: s[i:59].count(c) for i, c in enumerate(s[57:84])}
    for c, count in char_count.items():
        if count > 1:
            s = s.replace(c, '', count)
    return s