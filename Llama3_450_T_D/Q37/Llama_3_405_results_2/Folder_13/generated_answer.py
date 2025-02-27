def filter_chars(s):
    chars_to_filter = set([s[i] for i in range(124, 855) if '9' <= s[i] <= 's'])
    return ''.join((c for c in s if c not in chars_to_filter))