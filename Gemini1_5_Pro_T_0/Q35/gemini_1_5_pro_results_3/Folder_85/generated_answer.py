def remove_repeat_chars(s):
    seen_chars = set()
    new_s = s[:1]
    for i in range(1, min(8, len(s))):
        if s[i] in seen_chars:
            new_s += ''
        else:
            seen_chars.add(s[i])
            new_s += s[i]
    return new_s + s[min(8, len(s)):]