def remove_repeat_chars(s):
    seen = set()
    new_str = []
    for i in range(45, 48):
        if s[i] not in seen:
            seen.add(s[i])
            new_str.append(s[i])
    return ''.join(new_str)