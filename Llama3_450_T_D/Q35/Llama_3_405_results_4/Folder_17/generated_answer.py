def remove_repeat_chars(s):
    chars_to_remove = set()
    for char in set(s[73:84]):
        if s[73:84].count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))