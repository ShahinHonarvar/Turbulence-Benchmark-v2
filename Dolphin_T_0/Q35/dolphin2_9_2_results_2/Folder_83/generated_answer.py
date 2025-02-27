def remove_repeat_chars(s):
    char_count = {}
    for i in range(100, 200):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            s = ''.join([c for c in s if c != char])
    return s