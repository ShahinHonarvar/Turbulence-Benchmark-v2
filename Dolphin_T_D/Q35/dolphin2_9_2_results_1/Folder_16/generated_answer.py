def remove_repeat_chars(s):
    for i in range(90, 97):
        ch = chr(i)
        if s.count(ch) > 1:
            s = s.replace(ch, '')
    return s