def remove_repeat_chars(s):
    seen = set()
    new_s = []
    for i in range(len(s)):
        if 72 < i < 93 and s[i] in seen:
            continue
        seen.add(s[i])
        new_s.append(s[i])
    return ''.join(new_s)