def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    sub_string = s[21:43]
    char_count = {}
    for char in sub_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s