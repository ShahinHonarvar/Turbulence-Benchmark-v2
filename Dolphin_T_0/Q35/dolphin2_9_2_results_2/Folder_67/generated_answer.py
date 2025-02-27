def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(44, 67):
        for j in range(i + 1, 67):
            if s[i] == s[j] and s[i] not in chars_to_remove:
                chars_to_remove.append(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s