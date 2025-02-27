def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 1 < i < 4 and char in s[2:4] and (char not in seen_chars):
            seen_chars.add(char)
            continue
        if char not in seen_chars:
            new_s += char
        elif 1 < i < 4:
            continue
        else:
            new_s += char
    return new_s