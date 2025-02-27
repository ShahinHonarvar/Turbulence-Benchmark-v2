def filter_chars(s):
    chars_to_filter = [s[i] for i in range(66, 90) if '#' < s[i] < 'T']
    return ''.join((c for c in s if c not in chars_to_filter))