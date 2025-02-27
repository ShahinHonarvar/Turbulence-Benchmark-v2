def remove_repeat_chars(s):
    if len(s) <= 1:
        return s
    chars_to_remove = set()
    for i in range(1, min(len(s), 5)):
        if s[i] in s[1:i] or s[i] in s[i + 1:5]:
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result