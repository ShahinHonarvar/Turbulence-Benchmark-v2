def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if i > 0 and i < 6 and (char in s[1:6]) and (char in seen_chars):
            continue
        if i < 6 and char in s[1:6] and (char not in seen_chars):
            seen_chars.add(char)
        new_s += char
    return new_s