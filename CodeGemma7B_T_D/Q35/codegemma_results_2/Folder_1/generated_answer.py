def remove_repeat_chars(s):
    seen = set()
    new_s = []
    for i in range(17, 88):
        if s[i] not in seen:
            new_s.append(s[i])
            seen.add(s[i])
    return ''.join(new_s)