def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 90 > i or i > 97:
            new_s += char
        elif char not in seen_chars:
            if s[90:97].count(char) > 1:
                seen_chars.add(char)
            else:
                new_s += char
        else:
            continue
    return new_s