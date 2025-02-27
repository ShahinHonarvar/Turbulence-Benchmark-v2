def filter_chars(s):
    chars_to_remove = [c for c in s[71:95] if c >= 'K' and c <= 'a']
    return ''.join([ch for ch in s if ch not in chars_to_remove])