def remove_repeat_chars(s):
    char_count = {}
    indices = []
    for i in range(36, 54):
        if s[i] not in char_count:
            char_count[s[i]] = 1
        else:
            char_count[s[i]] += 1
            if char_count[s[i]] > 1:
                indices.append(s[i])
    for char in indices:
        s = s.replace(char, '')
    return s