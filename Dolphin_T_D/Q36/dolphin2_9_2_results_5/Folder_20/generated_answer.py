def filter_chars(s):
    chars_to_remove = [s[i] for i in range(13, 40) if ':' < s[i] < 'C']
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s