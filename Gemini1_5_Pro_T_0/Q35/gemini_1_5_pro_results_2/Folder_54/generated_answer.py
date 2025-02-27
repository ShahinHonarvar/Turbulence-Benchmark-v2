def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 35 < i < 64 and s.count(char) > 1:
            if char not in seen_chars:
                seen_chars.add(char)
        else:
            new_s += char
    return new_s