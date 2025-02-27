def filter_chars(s):
    s = list(s)
    chars_to_remove = [s[i] for i in range(33, 36) if '>' < s[i] < 'A']
    s = [c for c in s if c not in chars_to_remove]
    return ''.join(s)