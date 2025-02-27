def remove_repeat_chars(s):
    char_count = {}
    for i in range(56, 88):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    new_str = ''
    for char in s:
        if char_count.get(char, 0) <= 1:
            new_str += char
    return new_str