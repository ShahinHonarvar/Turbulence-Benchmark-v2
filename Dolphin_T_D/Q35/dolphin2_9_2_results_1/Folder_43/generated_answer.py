def remove_repeat_chars(s):
    chars_to_remove = {}
    for i in range(10, 28):
        if s[i] in chars_to_remove:
            chars_to_remove[s[i]] += 1
        else:
            chars_to_remove[s[i]] = 1
    for char in chars_to_remove:
        if chars_to_remove[char] > 1:
            s = s.replace(char, '')
    return s