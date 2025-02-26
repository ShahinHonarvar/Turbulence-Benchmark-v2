def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    section = s[34:78]
    to_remove = set()
    for char in section:
        if section.count(char) > 1 and char not in to_remove:
            to_remove.add(char)
    result = ''.join((char for char in s if char not in to_remove or s.index(char) <= 33 or s.index(char) >= 78))
    return result