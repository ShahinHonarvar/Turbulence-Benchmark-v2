def remove_repeat_chars(s):
    repeat_chars = {}
    for i in range(2, 5):
        if s[i] in repeat_chars:
            repeat_chars[s[i]] += 1
        else:
            repeat_chars[s[i]] = 1
    for char in repeat_chars:
        if repeat_chars[char] > 1:
            s = s.replace(char, '')
    return s