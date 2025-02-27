def remove_repeat_chars(s):
    char_count = {}
    for i in range(33, 78):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    new_s = ''
    for char in s:
        if char_count.get(char, 0) <= 1:
            new_s += char
    return new_s