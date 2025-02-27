def remove_repeat_chars(s):
    seen_chars = set()
    for i in range(51, 76):
        if s[i] in seen_chars:
            s = s.replace(s[i], '')
        else:
            seen_chars.add(s[i])
    return s