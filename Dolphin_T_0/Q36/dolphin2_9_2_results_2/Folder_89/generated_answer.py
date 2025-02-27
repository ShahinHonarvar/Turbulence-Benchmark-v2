def filter_chars(s):
    chars_to_remove = [s[i] for i in range(57, 69) if s[i] > '(' and s[i] < 'W']
    return ''.join([c for c in s if c not in chars_to_remove])