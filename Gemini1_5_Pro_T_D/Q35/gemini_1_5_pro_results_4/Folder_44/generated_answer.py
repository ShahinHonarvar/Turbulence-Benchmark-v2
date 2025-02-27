def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 36 < i < 52:
            if char in seen_chars:
                continue
            elif s[36:52].count(char) > 1:
                seen_chars.add(char)
                continue
            else:
                new_s += char
            continue
        new_s += char
    return new_s