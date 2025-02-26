def remove_repeat_chars(s):
    if len(s) <= 16:
        return s
    section = s[17:87]
    repeat_chars = set()
    for char in section:
        if section.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 17 or s.index(char) >= 87))
    return result