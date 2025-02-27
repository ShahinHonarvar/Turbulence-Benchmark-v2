def remove_repeat_chars(s):
    seen = set()
    new_str = ''
    for i in range(11, 76):
        if s[i] not in seen:
            seen.add(s[i])
            new_str += s[i]
    return new_str