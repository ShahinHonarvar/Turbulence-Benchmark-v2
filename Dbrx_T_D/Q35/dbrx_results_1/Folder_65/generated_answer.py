def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[51:76])
    for char in chars_to_remove:
        s = s.replace(char, '', s[50:77].count(char))
    return s[:51] + ''.join((c for c in s[51:76] if c not in chars_to_remove)) + s[76:]