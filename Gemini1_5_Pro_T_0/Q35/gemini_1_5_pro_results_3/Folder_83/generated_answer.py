def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(101, 199):
        if s.count(s[i]) > 1:
            repeated_chars.add(s[i])
    for char in repeated_chars:
        s = s.replace(char, '')
    return s