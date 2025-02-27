def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 2 < i < 7:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        new_s += char
    return new_s