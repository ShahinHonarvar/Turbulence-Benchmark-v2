def remove_repeat_chars(s):
    char_count = {}
    for i in range(46, 91):
        char = chr(i)
        if s.count(char) > 1:
            char_count[char] = 1
    return ''.join([c for c in s if c not in char_count])