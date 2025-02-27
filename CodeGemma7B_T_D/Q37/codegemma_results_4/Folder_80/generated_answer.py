def filter_chars(s):
    return ''.join((c for c in s if c < 'a' or c > 'i' or c < s[36] or (c > s[79])))