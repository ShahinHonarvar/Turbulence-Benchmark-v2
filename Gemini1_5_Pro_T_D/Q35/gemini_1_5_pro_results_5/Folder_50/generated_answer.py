def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 13 < i < 76:
            if char in seen_chars:
                continue
            elif s.count(char, 14, 76) > 1:
                seen_chars.add(char)
                continue
        new_s += char
    return new_s