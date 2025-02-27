def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i in range(len(s)):
        if 20 < i < 51:
            if s[i] in seen_chars:
                continue
            elif s.count(s[i]) > 1:
                seen_chars.add(s[i])
                continue
        new_s += s[i]
    return new_s