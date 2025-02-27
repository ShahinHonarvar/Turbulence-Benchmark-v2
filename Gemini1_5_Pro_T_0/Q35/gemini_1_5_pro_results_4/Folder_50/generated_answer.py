def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 13 < i < 76 and char in s[14:i]:
            if char not in seen_chars:
                seen_chars.add(char)
        else:
            new_s += char
    return new_s