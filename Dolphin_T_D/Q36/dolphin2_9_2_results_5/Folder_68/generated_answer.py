def filter_chars(s):
    chars_to_remove = [s[i] for i in range(1, 9) if '8' < s[i] < 'm']
    return ''.join([ch for ch in s if ch not in chars_to_remove])