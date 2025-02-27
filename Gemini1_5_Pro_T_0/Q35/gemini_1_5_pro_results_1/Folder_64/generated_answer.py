def remove_repeat_chars(s):
    seen_chars = set()
    new_s = ''
    for i in range(len(s)):
        if i > 0 and i < 5 and (s[i] in seen_chars):
            continue
        if i > 0 and i < 5 and (s[i] not in seen_chars):
            seen_chars.add(s[i])
        new_s += s[i]
    return new_s