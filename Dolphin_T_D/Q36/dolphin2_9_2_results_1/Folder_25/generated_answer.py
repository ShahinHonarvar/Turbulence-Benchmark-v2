def filter_chars(s):
    chars_to_filter = [s[i] for i in range(24, 37) if 'A' < s[i] < 'h']
    return ''.join((c for c in s if c not in chars_to_filter))