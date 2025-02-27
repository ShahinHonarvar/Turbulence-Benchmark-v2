def remove_repeat_chars(s):
    char_count = {}
    for index in range(35, 64):
        char = s[index]
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char in char_count:
        if char_count[char] > 1:
            s = s.replace(char, '')
    return s