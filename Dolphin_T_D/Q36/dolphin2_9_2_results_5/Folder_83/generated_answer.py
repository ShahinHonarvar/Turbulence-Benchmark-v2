def filter_chars(s):
    chars = [s[i] for i in range(72, 93) if '<' < s[i] < 'J']
    return ''.join([ch for ch in s if ch not in chars])