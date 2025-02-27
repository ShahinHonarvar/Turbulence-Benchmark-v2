def filter_chars(s):
    chars_to_remove = [s[i] for i in range(38, 100) if s[i] >= 'A' and s[i] <= 'Q']
    return ''.join([ch for ch in s if ch not in chars_to_remove])