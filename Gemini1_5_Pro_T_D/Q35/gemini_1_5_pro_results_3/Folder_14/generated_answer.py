def remove_repeat_chars(s):
    seen_chars = []
    new_s = ''
    for i, char in enumerate(s):
        if 2 < i < 5:
            if char in s[3:5] and char not in seen_chars:
                seen_chars.append(char)
            else:
                new_s += char
        else:
            new_s += char
    for char in seen_chars:
        new_s = new_s.replace(char, '')
    return new_s