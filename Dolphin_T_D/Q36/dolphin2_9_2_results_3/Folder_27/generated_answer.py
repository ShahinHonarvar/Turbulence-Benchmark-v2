def filter_chars(s):
    s_filtered = [ch for ch in s if 48 <= ord(ch) <= 75 and ch > '6' and (ch < '_')]
    return ''.join(s_filtered)