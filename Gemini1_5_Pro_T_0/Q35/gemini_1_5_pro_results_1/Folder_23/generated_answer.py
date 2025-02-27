def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i in range(len(s)):
        if i > 20 and i < 36:
            if s[i] in seen_chars:
                continue
            else:
                seen_chars.add(s[i])
        new_s += s[i]
    return new_s