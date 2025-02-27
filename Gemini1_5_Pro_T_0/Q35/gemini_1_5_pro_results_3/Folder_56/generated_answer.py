def remove_repeat_chars(s):
    seen_chars = []
    new_s = ''
    for i in range(len(s)):
        if 7 < i < 9:
            if s[i] in s[8:9] and s[i] not in seen_chars:
                seen_chars.append(s[i])
            else:
                new_s += s[i]
        elif s[i] not in seen_chars:
            new_s += s[i]
    return new_s