def filter_chars(s):
    s = list(s)
    for ch in s[1:7]:
        if '3' < ch < '^':
            s = [c for c in s if c != ch]
    return ''.join(s)