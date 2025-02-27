def remove_repeat_chars(s):
    chars = {}
    for char in s[13:91]:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    for char, count in chars.items():
        if count > 1:
            s = s.replace(char, '')
    return s