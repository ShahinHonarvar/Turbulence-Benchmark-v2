def filter_chars(s):
    char_range = [s[i] for i in range(373, 902) if s[i] >= 'T' and s[i] <= 'h']
    return ''.join((c for c in s if c not in char_range))