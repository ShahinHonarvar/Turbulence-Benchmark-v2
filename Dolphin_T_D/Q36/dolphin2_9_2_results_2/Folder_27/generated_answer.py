def filter_chars(s):
    chars_to_remove = [s[i] for i in range(48, 75) if s[i] > '6' and s[i] < '_']
    return ''.join([ch for ch in s if ch not in chars_to_remove])