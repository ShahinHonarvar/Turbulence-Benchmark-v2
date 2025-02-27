def remove_repeat_chars(s):
    chars = [s[i] for i in range(1, 9) if s.count(s[i]) > 1]
    for char in chars:
        s = s.replace(char, '')
    return s