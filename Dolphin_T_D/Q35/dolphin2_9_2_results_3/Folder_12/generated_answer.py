def remove_repeat_chars(s):
    to_remove = set()
    for i in range(16, 87):
        if s[i] in to_remove:
            s = s.replace(s[i], '')
        else:
            to_remove.add(s[i])
    return s