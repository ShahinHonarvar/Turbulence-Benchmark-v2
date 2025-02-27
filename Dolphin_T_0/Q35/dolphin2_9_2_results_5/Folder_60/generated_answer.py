def remove_repeat_chars(s):
    duplicate_chars = set()
    for i in range(38, 52):
        if s[i] in s[i + 1:52]:
            duplicate_chars.add(s[i])
    for duplicate_char in duplicate_chars:
        s = s.replace(duplicate_char, '')
    return s