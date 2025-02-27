def remove_repeat_chars(s):
    seen = set()
    new_s = ''
    for i, char in enumerate(s):
        if i in range(1, 9):
            if char in seen:
                continue
            elif s.count(char) > 1:
                seen.add(char)
                continue
            else:
                new_s += char
        else:
            new_s += char
    return new_s