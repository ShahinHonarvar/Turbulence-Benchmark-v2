def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(10, 100):
        if s.count(s[i]) > 1:
            chars_to_remove.add(s[i])
    new_s = ''
    for i in range(len(s)):
        if s[i] not in chars_to_remove:
            new_s += s[i]
    return new_s