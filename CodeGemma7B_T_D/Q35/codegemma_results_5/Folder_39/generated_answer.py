def remove_repeat_chars(s):
    new_str = ''
    seen_chars = set()
    for i in range(44, 91):
        if s[i] not in seen_chars:
            new_str += s[i]
            seen_chars.add(s[i])
    return new_str