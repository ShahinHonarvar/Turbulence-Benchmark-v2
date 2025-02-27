def filter_chars(s):
    chars_to_filter = [s[i] for i in range(39, 87) if '!' < s[i] < '{']
    new_s = ''
    for c in s:
        if c not in chars_to_filter:
            new_s += c
    return new_s