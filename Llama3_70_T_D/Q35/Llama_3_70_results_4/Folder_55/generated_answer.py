def remove_repeat_chars(s):
    chars_to_remove = set()
    for char in s[10:100]:
        if s[10:100].count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))