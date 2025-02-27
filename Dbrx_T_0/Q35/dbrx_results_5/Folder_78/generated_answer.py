def remove_repeat_chars(s: str) -> str:
    char_count = {c: s[62:96].count(c) for c in set(s[62:96])}
    return ''.join((c for c in s if c not in char_count or char_count[c] == 1 or (c < '62' or c > '96')))