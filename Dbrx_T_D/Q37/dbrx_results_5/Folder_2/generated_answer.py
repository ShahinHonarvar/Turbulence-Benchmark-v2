def filter_chars(s):
    filtered_chars = [c for c in s if 477 <= s.index(c) <= 984 and ord(',') <= ord(c) <= ord('V')]
    return ''.join([c for c in s if c not in filtered_chars])