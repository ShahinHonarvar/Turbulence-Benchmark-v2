def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 46 < i < 91:
            if char in seen_chars:
                continue
            elif s.count(char, 47, 91) > 1:
                seen_chars.add(char)
                continue
            else:
                new_s += char
        else:
            new_s += char
    return new_s