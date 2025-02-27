def remove_repeat_chars(s):
    char_count = {}
    for i in range(90, 200):
        char = s[i]
        if char in char_count and char_count[char] == 1:
            s = s.replace(char, '')
        char_count[char] = char_count.get(char, 0) + 1
    return s