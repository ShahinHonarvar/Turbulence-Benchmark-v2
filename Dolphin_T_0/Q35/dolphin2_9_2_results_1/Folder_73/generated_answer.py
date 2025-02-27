def remove_repeat_chars(s):
    unique_chars = {}
    for i in range(10, 76):
        if s[i] in unique_chars:
            unique_chars[s[i]] += 1
        else:
            unique_chars[s[i]] = 1
    for char in unique_chars:
        if unique_chars[char] > 1:
            s = s.replace(char, '')
    return s