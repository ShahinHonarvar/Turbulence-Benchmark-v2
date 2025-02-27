def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 90 < i < 97:
            if char in seen_chars:
                continue
            elif s[i + 1:97].count(char) > 0:
                seen_chars.add(char)
                continue
            else:
                new_s += char
            continue
        new_s += char
    return new_s