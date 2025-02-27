def remove_repeat_chars(s):
    for char in s[62:96]:
        if s.count(char) > s[62:96].count(char):
            s = s.replace(char, '', s.count(char) - s[62:96].count(char))
    return s