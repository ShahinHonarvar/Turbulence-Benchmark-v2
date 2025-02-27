def filter_chars(s):
    to_remove = set()
    for i in range(588, 648):
        if i < len(s) and ',' < s[i] < 'c':
            to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in to_remove))