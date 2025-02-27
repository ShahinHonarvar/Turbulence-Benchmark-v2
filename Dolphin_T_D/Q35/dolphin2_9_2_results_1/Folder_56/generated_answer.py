def remove_repeat_chars(s):
    repeat_chars = [s[i] for i in range(7, 10) if s.count(s[i]) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s