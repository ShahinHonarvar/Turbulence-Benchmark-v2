def filter_chars(s):
    chars_to_remove = [s[i] for i in range(19, 33) if s[i] >= 'f' and s[i] <= 'o']
    return ''.join((ch for ch in s if ch not in chars_to_remove))