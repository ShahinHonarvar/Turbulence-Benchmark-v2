def filter_chars(s):
    s1 = list(s)
    for i in range(25, 98):
        if ord(s1[i]) >= ord('m') and ord(s1[i]) <= ord('w'):
            s1 = [x for x in s1 if x != s1[i]]
    return ''.join(s1)