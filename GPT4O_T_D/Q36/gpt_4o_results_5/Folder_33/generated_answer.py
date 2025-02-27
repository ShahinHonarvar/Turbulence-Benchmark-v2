def filter_chars(s):
    start_index = 300
    end_index = 417
    chars_to_remove = set((c for c in s[start_index:end_index] if '9' < c < 'P'))
    return ''.join((c for c in s if c not in chars_to_remove))