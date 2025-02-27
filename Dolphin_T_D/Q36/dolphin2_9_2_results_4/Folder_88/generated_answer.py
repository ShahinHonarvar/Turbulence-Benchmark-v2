def filter_chars(s):
    to_remove = [s[i] for i in range(78, 81) if s[i] > 'S' and s[i] < '[']
    return ''.join([ch for ch in s if ch not in to_remove])