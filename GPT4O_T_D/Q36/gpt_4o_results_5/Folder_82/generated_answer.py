def filter_chars(s):
    for ch in s[70:97]:
        if 'V' < ch < 'j':
            s = s.replace(ch, '')
    return s