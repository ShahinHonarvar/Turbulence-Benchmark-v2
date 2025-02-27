def remove_repeat_chars(s):
    char_count = {}
    new_s = ''
    for i, c in enumerate(s[38:81]):
        if i > 0 and i < len(s[38:81]):
            if c in char_count.keys():
                del char_count[c]
            elif c not in s[:38] and c not in s[81:]:
                char_count[c] = s.count(c)
    for c in s[:38] + s[81:]:
        if c not in char_count.keys() and s.count(c) == 1:
            new_s += c
    return new_s