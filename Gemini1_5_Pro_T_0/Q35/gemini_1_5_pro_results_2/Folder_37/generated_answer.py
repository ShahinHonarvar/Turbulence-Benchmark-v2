def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 2 < i < 7:
            if char in seen_chars:
                continue
            elif s[i + 1:].count(char) > 0:
                seen_chars.add(char)
                continue
        new_s += char
    return new_s