def filter_chars(s):
    to_remove = [s[i] for i in range(55, 66) if 'f' < s[i] < '|']
    s = ''.join([ch for ch in s if ch not in to_remove])
    return s