def filter_chars(s):
    chars = [s[i] for i in range(26, 80) if s[i] > '<' and s[i] < '>']
    return ''.join([ch for ch in s if ch not in chars])