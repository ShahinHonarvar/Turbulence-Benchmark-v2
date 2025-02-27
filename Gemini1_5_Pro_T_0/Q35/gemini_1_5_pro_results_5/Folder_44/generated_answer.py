def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if i > 36 and i < 52 and (char in s[37:51]):
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        new_s += char
    return new_s