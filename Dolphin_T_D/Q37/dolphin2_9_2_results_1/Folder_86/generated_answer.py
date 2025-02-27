def filter_chars(s):
    to_remove = set()
    for i in range(164, 707):
        if s[i] >= 'O' and s[i] <= '}':
            to_remove.add(s[i])
    return ''.join([ch for ch in s if ch not in to_remove])