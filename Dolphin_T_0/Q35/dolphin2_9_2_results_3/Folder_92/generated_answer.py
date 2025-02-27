def remove_repeat_chars(s):
    char_count = {}
    for i in range(len(s)):
        if i < 2:
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
    for key in char_count:
        if char_count[key] > 1:
            s = s.replace(key, '')
    return s