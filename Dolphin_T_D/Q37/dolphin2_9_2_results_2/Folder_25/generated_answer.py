def filter_chars(s):
    chars_to_remove = [s[i] for i in range(31, 39) if ';' <= s[i] <= 'g']
    return ''.join([ch for ch in s if ch not in chars_to_remove])