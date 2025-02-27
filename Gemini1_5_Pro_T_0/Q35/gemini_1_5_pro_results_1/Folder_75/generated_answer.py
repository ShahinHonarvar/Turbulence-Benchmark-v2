def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 20 < i < 51:
            if char in seen_chars:
                continue
            elif s[21:51].count(char) > 1:
                seen_chars.add(char)
                continue
            else:
                new_s += char
            continue
        new_s += char
    return new_s