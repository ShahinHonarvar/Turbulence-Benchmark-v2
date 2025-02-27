def remove_repeat_chars(s):
    seen = set()
    for i in range(16, 87):
        if s[i] in s[17:87] and s[i] not in seen:
            seen.add(s[i])
            s = s.replace(s[i], '')
    return s