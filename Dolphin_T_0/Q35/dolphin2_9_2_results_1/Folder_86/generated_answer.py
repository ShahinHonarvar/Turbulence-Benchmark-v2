def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(19, 32):
        for j in range(i + 1, 32):
            if s[i] == s[j]:
                chars_to_remove.add(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s