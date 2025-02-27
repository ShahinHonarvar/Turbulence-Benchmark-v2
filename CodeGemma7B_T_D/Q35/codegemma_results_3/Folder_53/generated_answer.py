def remove_repeat_chars(s):
    seen_chars = set()
    new_str = ''
    for i, c in enumerate(s):
        if i >= 200 and i < 202:
            if c not in seen_chars:
                seen_chars.add(c)
                new_str += c
        else:
            new_str += c
    return new_str