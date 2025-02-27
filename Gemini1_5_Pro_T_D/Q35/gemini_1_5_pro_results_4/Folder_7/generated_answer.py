def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 375 < i < 926:
            if char in seen_chars:
                continue
            elif s.count(char, 376, 926) > 1:
                seen_chars.add(char)
                continue
        new_s += char
    return new_s