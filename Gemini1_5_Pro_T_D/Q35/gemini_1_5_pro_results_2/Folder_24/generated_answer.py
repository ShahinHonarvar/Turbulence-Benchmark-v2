def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 13 < i < 91 and s.count(char) > 1:
            if char not in seen_chars:
                seen_chars.add(char)
                new_s += char
        else:
            new_s += char
    return new_s