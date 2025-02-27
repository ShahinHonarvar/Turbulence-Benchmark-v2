def filter_chars(s):
    for i in range(163, 658):
        char = s[i]
        if ord('()') < ord(char) < ord(']'):
            s = s.replace(char, '')
    return s[163:658]