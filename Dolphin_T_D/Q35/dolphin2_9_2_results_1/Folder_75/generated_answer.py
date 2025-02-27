def remove_repeat_chars(s):
    char_to_remove = set()
    for i in range(20, 51):
        if s.count(s[i]) > 1:
            char_to_remove.add(s[i])
    new_s = ''
    for i in range(len(s)):
        if s[i] not in char_to_remove:
            new_s += s[i]
    return new_s