def filter_chars(s):
    chars_to_remove = [s[i] for i in range(170, 195) if s[i] > '!' and s[i] < '{']
    return ''.join([ch for ch in s if ch not in chars_to_remove])