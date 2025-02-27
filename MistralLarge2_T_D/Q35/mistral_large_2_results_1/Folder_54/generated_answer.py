def remove_repeat_chars(s):
    char_count = {}
    for i in range(35, 64):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    for char in char_count:
        if char_count[char] > 1:
            s = s.replace(char, '')
    return s