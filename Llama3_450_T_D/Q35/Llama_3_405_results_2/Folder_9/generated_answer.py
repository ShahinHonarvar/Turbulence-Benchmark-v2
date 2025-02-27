def remove_repeat_chars(s):
    s = list(s)
    char_count = {}
    for i in range(80, 200):
        if i < len(s):
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            s = [c for c in s if c != char]
    return ''.join(s)