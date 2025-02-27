def filter_chars(s):
    chars_to_remove = [s[i] for i in range(21, 25) if s[i] > '5' and s[i] < '}']
    new_s = ''.join([c for c in s if c not in chars_to_remove])
    return new_s