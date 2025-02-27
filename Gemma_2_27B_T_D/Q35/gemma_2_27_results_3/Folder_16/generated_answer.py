def remove_repeat_chars(s):
    seen = set()
    to_remove = set()
    for i in range(90, 97):
        if s[i] in seen:
            to_remove.add(s[i])
        else:
            seen.add(s[i])
    for char in to_remove:
        s = s.replace(char, '')
    return s