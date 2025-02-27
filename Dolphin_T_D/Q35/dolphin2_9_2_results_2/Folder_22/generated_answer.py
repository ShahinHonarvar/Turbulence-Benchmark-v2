def remove_repeat_chars(s):
    char_count = {}
    for i in range(50, 200):
        char = s[i]
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s