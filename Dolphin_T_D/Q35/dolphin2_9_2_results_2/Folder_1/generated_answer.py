def remove_repeat_chars(s):
    indices = set()
    for i in range(len(s)):
        if s[i] not in s[17:88] and s[i] not in indices:
            indices.add(s[i])
    new_s = ''
    for i in range(len(s)):
        if s[i] not in s[17:88] or s[i] in indices:
            new_s += s[i]
    return new_s