def remove_repeat_chars(s):
    seen_chars = set()
    new_s = list(s)
    for i in range(2, min(6, len(s))):
        if s[i] in seen_chars:
            new_s[i] = ''
        else:
            seen_chars.add(s[i])
    return ''.join(new_s)