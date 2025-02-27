def remove_repeat_chars(s):
    chars_to_remove = {}
    for i in range(5):
        if s[i] in chars_to_remove:
            continue
        if s.count(s[i]) > 1:
            chars_to_remove[s[i]] = True
    return ''.join((c for c in s if c not in chars_to_remove))