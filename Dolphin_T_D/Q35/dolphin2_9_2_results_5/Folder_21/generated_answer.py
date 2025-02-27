def remove_repeat_chars(s):
    chars = {}
    for i in range(462, 995):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    for char, count in chars.items():
        if count > 1:
            s = s.replace(char, '')
    return s