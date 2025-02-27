def remove_repeat_chars(s):
    chars = {}
    for i in range(20, 37):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    for char in chars:
        if chars[char] > 1:
            s = s.replace(char, '')
    return s