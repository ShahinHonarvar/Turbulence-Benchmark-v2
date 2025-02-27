def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 56 < i < 88:
            if char in seen_chars:
                continue
            elif s.count(char, 56, 88) > 1:
                seen_chars.add(char)
                continue
            else:
                new_s += char
            continue
        new_s += char
    return new_s