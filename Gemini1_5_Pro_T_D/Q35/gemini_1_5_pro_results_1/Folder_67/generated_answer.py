def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 44 < i < 67:
            if char in seen_chars:
                continue
            elif s[45:67].count(char) > 1:
                seen_chars.add(char)
                continue
        new_s += char
    return new_s