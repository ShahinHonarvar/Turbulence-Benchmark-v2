def remove_repeat_chars(s):
    seen_chars = []
    new_s = ''
    for i, char in enumerate(s):
        if 7 < i < 9:
            if char in s[8:9] and char not in seen_chars:
                seen_chars.append(char)
            else:
                seen_chars.append(char)
                new_s += char
        elif char not in seen_chars:
            new_s += char
    return new_s