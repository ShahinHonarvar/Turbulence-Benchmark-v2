def remove_repeat_chars(s):
    char_count = {}
    for char in s[1:9]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in char_count:
        if char_count[char] > 1:
            s = s.replace(char, '')
    return s