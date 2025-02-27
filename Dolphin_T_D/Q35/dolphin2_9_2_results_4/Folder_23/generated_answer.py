def remove_repeat_chars(s):
    char_count = {}
    for i in range(20, 36):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in char_count:
        if char_count[char] > 1:
            s = s.replace(char, '')
    return s