def filter_chars(s):
    chars_to_remove = [s[i] for i in range(163, 658) if s[i] > '(' and s[i] < ']']
    return ''.join([c for c in s if c not in chars_to_remove])