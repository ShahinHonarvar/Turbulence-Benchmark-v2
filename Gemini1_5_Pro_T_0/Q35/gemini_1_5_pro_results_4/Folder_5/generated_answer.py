def remove_repeat_chars(s):
    seen_chars = set()
    new_s = s[:2]
    for i in range(2, min(8, len(s))):
        if s[i] in seen_chars:
            continue
        seen_chars.add(s[i])
        if s.count(s[i]) > 1:
            continue
        new_s += s[i]
    new_s += s[min(8, len(s)):]
    return new_s