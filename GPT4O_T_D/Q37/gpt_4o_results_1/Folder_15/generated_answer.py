def filter_chars(s):
    remove_chars = {s[i] for i in range(2, min(7, len(s))) if '?' <= s[i] <= 'f'}
    return ''.join((ch for ch in s if ch not in remove_chars))