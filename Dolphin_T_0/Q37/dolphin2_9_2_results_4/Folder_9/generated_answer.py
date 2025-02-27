def filter_chars(s):
    chars_to_remove = [s[i] for i in range(38, 100) if s[i] >= 'A' and s[i] <= 'Q']
    return ''.join([c for c in s if c not in chars_to_remove])