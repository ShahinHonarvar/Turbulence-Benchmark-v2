def remove_repeat_chars(s):
    s1 = s[:68]
    s2 = s[68:99]
    s3 = s[99:]
    for char in set(s2):
        if s2.count(char) > 1:
            s1 = s1.replace(char, '')
            s2 = s2.replace(char, '')
            s3 = s3.replace(char, '')
    return s1 + s2 + s3