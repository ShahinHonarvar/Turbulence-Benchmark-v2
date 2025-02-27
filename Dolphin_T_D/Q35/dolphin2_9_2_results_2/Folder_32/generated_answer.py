def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(86, 90):
        if s[i] in s[i + 1:90]:
            chars_to_remove.append(s[i])
    s = ''.join((c for c in s if c not in chars_to_remove))
    return s