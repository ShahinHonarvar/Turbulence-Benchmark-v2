def filter_chars(s):
    chars_to_remove = [s[i] for i in range(4, 8) if '1' < s[i] < 'J']
    return ''.join((c for c in s if c not in chars_to_remove))