def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 11):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s