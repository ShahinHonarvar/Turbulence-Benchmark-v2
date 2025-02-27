def filter_chars(s):
    for ch in range(ord(')'), ord('P')):
        if chr(ch) in s[18:38]:
            s = s.replace(chr(ch), '')
    return s