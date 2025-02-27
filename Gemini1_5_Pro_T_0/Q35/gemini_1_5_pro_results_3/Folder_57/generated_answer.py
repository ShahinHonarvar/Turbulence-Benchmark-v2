def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 25 < i < 80:
            if char in seen_chars:
                continue
            elif s[25:80].count(char) > 1:
                seen_chars.add(char)
                continue
            else:
                new_s += char
        else:
            new_s += char
    return new_s