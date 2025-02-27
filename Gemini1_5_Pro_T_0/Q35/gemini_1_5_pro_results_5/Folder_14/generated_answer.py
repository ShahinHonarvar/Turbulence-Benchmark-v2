def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i, char in enumerate(s):
        if 2 < i < 5:
            if char in seen_chars:
                continue
            else:
                if s.count(char) > 1:
                    seen_chars.add(char)
                new_s += char
        else:
            new_s += char
    return new_s