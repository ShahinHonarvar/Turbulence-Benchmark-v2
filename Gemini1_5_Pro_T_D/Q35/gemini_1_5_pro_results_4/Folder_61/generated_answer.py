def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if i > 0 and i < 8 and (char in s[1:8]) and (char not in seen_chars):
            seen_chars.add(char)
        if char not in seen_chars:
            new_s += char
    return new_s