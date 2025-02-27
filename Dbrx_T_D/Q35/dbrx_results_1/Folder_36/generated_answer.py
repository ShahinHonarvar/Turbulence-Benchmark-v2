def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[476:709])
    for c in chars_to_remove:
        if s[476:709].count(c) > 1:
            s = s[:476] + ''.join((d for d in s[476:709] if d != c)) + s[709:]
    return s