def remove_repeat_chars(s):
    to_remove = []
    for i in range(355, 988):
        if s[i] in s[i + 1:988]:
            to_remove.append(s[i])
    for ch in to_remove:
        s = s.replace(ch, '')
    return s