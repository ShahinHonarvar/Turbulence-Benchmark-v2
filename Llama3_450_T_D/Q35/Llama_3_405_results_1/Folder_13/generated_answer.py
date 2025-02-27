def remove_repeat_chars(s):
    char_counts = {}
    for i in range(46, 91):
        if s.count(chr(i)) > 1:
            char_counts[chr(i)] = s.count(chr(i))
    for char in char_counts:
        s = s.replace(char, '')
    return s