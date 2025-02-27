def remove_repeat_chars(s):
    c = s[43:70]
    d = ''.join((i for i in c if c.count(i) == 1))
    return s[:43] + s[43:70].translate(str.maketrans('', '', d)) + s[70:]